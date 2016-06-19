from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Count, F
from .models import Transaction, TransactionHistory, Person, Item, Category
from .forms import TransactionForm, ItemForm, PersonForm
from django.http import HttpRequest, HttpResponse
from datetime import datetime, timedelta, date

from django.http import HttpResponseRedirect
from django.template.context_processors import csrf

def home(request):
	open_transactions = Transaction.objects.filter(time_out__isnull=False).values_list('person', flat=True)
	borrowers = Person.objects.filter(pk__in=[x for x in open_transactions]).order_by('last_name')

	return render(request, 'checkout/home.html', {'borrowers': borrowers})


def display_checkout(request, status="", person="", id_number="", inventory_tag=""):	
	people = Person.objects.all()
	inventory = Item.objects.all()

	if request.method == "POST":
		if id_number == "":
			id_number = request.POST.get('id_number')
		if inventory_tag == "":
			inventory_tag = request.POST.get('inventory_tag')
	else:
		return render(request, 'checkout/checkout.html', {'status': status, 'people': people})

	if id_number <> "":
		try:
			person = Person.objects.get(id_number__iexact=id_number)
			status = "Person.Success"

			if inventory_tag is not None and inventory_tag <> "":
				try:
					item = Item.objects.get(inventory_tag__iexact=inventory_tag)
					status = "Item.Success"

					try:
						transaction = Transaction.objects.get(item=item.pk)
						if transaction.person == person:
							status = "Transaction.Duplicate"
						else:
							status = "Transaction.Conflict"

					except Transaction.DoesNotExist:
						transaction = Transaction.objects.create(person=person, item=item)
						transaction.check_out()
						status = "Transaction.Success"

					return render(request, 'checkout/person_detail.html', {'status': status, 'inventory': inventory, 'person': person, 'id_number': id_number, 'inventory_tag': inventory_tag})

				except Item.DoesNotExist:
					status = "Item.DoesNotExist"
					
		except Person.DoesNotExist:
			status = "Person.DoesNotExist"
			return render(request, 'checkout/checkout.html', {'status': status, 'people': people})
	else:
		return render(request, 'checkout/checkout.html', {'status': status, 'people': people})

	return render(request, 'checkout/person_detail.html', {'status': status, 'inventory': inventory, 'person': person, 'id_number': id_number, 'inventory_tag': inventory_tag})
						

def person_search(request):
	result = ""
	barcode = ""
	if request.method == "POST":
		barcode = request.POST.get('barcode')
		if barcode <> "":
			try:
				person = Person.objects.get(id_number=barcode)
				return redirect('checkout.views.checkout_add', id_number=barcode)
			except Person.DoesNotExist:
				result = 1
	return display_checkout(request, result, barcode)


def quick_checkout(request, p):
			person = get_object_or_404(Person, pk=p)
			if request.method == "POST":
				barcode = request.POST.get('barcode')
				if barcode <> "":
					try:
						item = get_object_or_404(Item, inventory_tag=barcode)
						try:
							transaction = Transaction.objects.get(item=item.pk)
						except Transaction.DoesNotExist:
							transaction = Transaction.objects.create(person=person, item=item)
						transaction.check_out()
					except Item.DoesNotExist:
						result = 1
			return redirect('checkout.views.checkout_add', id_number=person.id_number)


def checkout_add(request, id_number):
    person = get_object_or_404(Person, id_number=id_number)
    transactions = Transaction.objects.all()
    people = Person.objects.all()
    item = Transaction.objects.filter(person=person.pk).filter(time_out__isnull=False)
    requests = Transaction.objects.filter(person=person.pk).filter(time_out__isnull=True)
    available_items = Item.objects.exclude(pk__in = [x for x in Transaction.objects.values_list('item', flat=True)])

    categories = Category.objects.all().order_by('name')

    history = TransactionHistory.objects.filter(person=person.pk)
    return render(request, 'checkout/checkout_add.html', {'people': people, 'categories': categories, 'person': person, 'item': item, 'requests': requests, 'available_items': available_items, 'history': history})


def loans(request):
		loans = Transaction.objects.filter(time_out__isnull=False)

		return render(request, 'checkout/loans.html', {'loans': loans})

def reports(request):
    transactions = Transaction.objects.all()
    history = TransactionHistory.objects.all()
    all_people = Person.objects.all()
    active_people = Person.objects.filter(pk__in=transactions)
    active_items = Item.objects.filter(pk__in=transactions)
    borrowers = Person.objects.filter(pk__in=history)
    loaned_items = Item.objects.filter(pk__in=history)
    history_category = history.values('item__category__name').annotate(count=Count("item")).order_by('-count')[:10]
    history_items = history.values('item__display_name', 'item__serial', 'item__pk').annotate(count=Count("item__pk")).order_by('-count')[:10]
    history_people = history.values('person__first_name', 'person__last_name', 'person__id_number').filter(person__active=True).annotate(count=Count("person")).order_by('-count')[:10]

    return render(request, 'checkout/reports.html', {'history': history, 'history_category': history_category, 'history_items': history_items, 'history_people': history_people, 'transactions': transactions, 'all_people': all_people, 'borrowers': borrowers, 'loaned_items': loaned_items, 'active_people': active_people, 'active_items': active_items})

def history(request, filter=''):
    if request.method == "POST":
        filter = request.POST.get('filter')
    history = TransactionHistory.objects.all().order_by('-time_in')
    return render(request, 'checkout/history.html', {'history': history, 'filter': filter})

def dashboard(request):
    loans = Person.objects.filter(pk__in=[x for x in Transaction.objects.filter(time_out__isnull=False).values_list('person', flat=True)])
    reservations = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=True).values_list('person', flat=True)])

    return render(request, 'checkout/dashboard.html', {'loans': loans, 'reservations': reservations})

def login(request):
    return render(request, 'checkout/login.html')

def person_list(request, tab='all'):
    people = Person.objects.filter(active=True)

    return render(request, 'checkout/person_list.html', {'people': people})


def person_detail(request, id_number):
    #person = get_object_or_404(Person, pk=pk)
    person = get_object_or_404(Person, id_number=id_number)
    transactions = Transaction.objects.all()
    item = Transaction.objects.filter(person=person.pk).filter(time_out__isnull=False)
    requests = Transaction.objects.filter(person=person.pk).filter(time_out__isnull=True)
    available_items = Item.objects.exclude(pk__in = [x for x in Transaction.objects.values_list('item', flat=True)])

    categories = Category.objects.all().order_by('name')

    history = TransactionHistory.objects.filter(person=person.pk)
    return render(request, 'checkout/person_detail.html', {'categories': categories, 'person': person, 'item': item, 'requests': requests, 'available_items': available_items, 'history': history})

def person_history(request, id_number):
    person = get_object_or_404(Person, id_number=id_number)
    requests = Transaction.objects.filter(person=person.pk).filter(time_out__isnull=True)
    item = Transaction.objects.filter(person=person.pk).filter(time_out__isnull=False)
    history = TransactionHistory.objects.filter(person=person.pk)
    return render(request, 'checkout/person_history.html', {'person': person, 'history': history, 'item': item})

def check_in(request):
    transactions = Transaction.objects.all()
    people = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=False).values_list('person', flat=True)])
    return render(request, 'checkout/check_in.html', {'people': people})
	
def item_search(request, pk):
    if request.method == "POST":
      #response = HttpResponse("You are searching for: " + request.POST.get('person', 'Bob'))
      #return response
      person = get_object_or_404(Person, pk=pk)
      item = get_object_or_404(Item, inventory_tag=request.POST.get('item', None))
      return request_item(request, p=person.pk, i=item.pk)
    else:
	  return person_detail(request, pk)
	  

def item_popup(request, pk):
    item = get_object_or_404(Item, pk=pk)
    transactions = Transaction.objects.all()
    history = TransactionHistory.objects.filter(item=pk)
    return render(request, 'checkout/item_popup.html', {'item': item, 'history': history})


def browse_items(request, id_number):
    person = get_object_or_404(Person, id_number=id_number)
    transactions = Transaction.objects.all()
    available_items = Item.objects.exclude(pk__in = [x for x in Transaction.objects.values_list('item', flat=True)])
    categories = Category.objects.all().order_by('name')
    return render(request, 'checkout/browse_items.html', {'categories': categories, 'person': person, 'available_items': available_items})


def item_list(request):
    inventory = Item.objects.all().order_by('category')
    return render(request, 'checkout/item_list.html', {'inventory': inventory})

def item_checkin(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    person = transaction.person
    item = transaction.item
    transaction.check_in()
#    return redirect('checkout.views.person_detail', id_number=person.id_number, status="Item.Returned")
    return render(request, 'checkout/person_detail.html', {'status': "Item.Returned", 'person': person, 'id_number': person.id_number, 'inventory_tag': item.inventory_tag})
# 	return render(request, 'checkout/person_detail.html', {'status': status, 'inventory': inventory, 'person': person, 'id_number': id_number, 'inventory_tag': inventory_tag})

def checkout_item(request, p, i):
    person = get_object_or_404(Person, pk=p)
    item = get_object_or_404(Item, pk=i)
    transaction = Transaction.objects.get(person=person, item=item)
    transaction.check_out()

    return redirect('checkout.views.person_detail', id_number=person.id_number)
        
def delete_transaction(request, t):
    transaction = get_object_or_404(Transaction, pk=t)
    person = transaction.person
    transaction.cancel_request()

    return redirect('checkout.views.person_detail', id_number=person.id_number)
    
    
def item_create(request):
    if request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
          form.save()
          
          return HttpResponseRedirect('/checkitout/items/all')
    else:
        form = ItemForm()
        
        args = {}
        args.update(csrf(request))
      
        args['form'] = form

        return render(request, 'checkout/item_create.html', args)    
        
def person_create(request):
    if request.POST:
        form = PersonForm(request.POST)
        if form.is_valid():
          form.save()
          
          return HttpResponseRedirect('/checkitout/students/all')
    else:
        form = PersonForm()
        
        args = {}
        args.update(csrf(request))
      
        args['form'] = form

        return render(request, 'checkout/person_create.html', args)    