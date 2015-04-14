from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Count, F
from .models import Transaction, TransactionHistory, Person, Catalog, Item, Category
from .forms import TransactionForm
from django.http import HttpRequest, HttpResponse

def reservations(request):
    transactions = Transaction.objects.all()
    all_people = Person.objects.all()
    active_people = Person.objects.filter(pk__in=[x for x in Transaction.objects.filter(time_out__isnull=True).values_list('person', flat=True)])
    requests = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=True).values_list('person', flat=True)])
    active_items = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=False).values_list('person', flat=True)])

    return render(request, 'checkout/reservations.html', {'transactions': transactions, 'all_people': all_people, 'active_people': active_people, 'active_items': active_items, 'requests': requests})

def on_loan(request):
    transactions = Transaction.objects.all()
    all_people = Person.objects.all()
    active_people = Person.objects.filter(pk__in=[x for x in Transaction.objects.filter(time_out__isnull=False).values_list('person', flat=True)])
    requests = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=True).values_list('person', flat=True)])
    active_items = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=False).values_list('person', flat=True)])

    return render(request, 'checkout/on_loan.html', {'transactions': transactions, 'all_people': all_people, 'active_people': active_people, 'active_items': active_items, 'requests': requests})

def search(request):
    transactions = Transaction.objects.all()
    all_people = Person.objects.all()
    active_people = Person.objects.filter(pk__in=transactions)
    active_items = Item.objects.filter(pk__in=transactions)
    return render(request, 'checkout/search.html', {'transactions': transactions, 'all_people': all_people, 'active_people': active_people, 'active_items': active_items})

def reports(request):
    transactions = Transaction.objects.all()
    history = TransactionHistory.objects.all()
    all_people = Person.objects.all()
    active_people = Person.objects.filter(pk__in=transactions)
    active_items = Item.objects.filter(pk__in=transactions)
    borrowers = Person.objects.filter(pk__in=history)
    loaned_items = Item.objects.filter(pk__in=history)
    history_category = history.values('item__category__name').annotate(count=Count("item")).order_by('-count')
    history_items = history.values('item__brand__name', 'item__model', 'item__serial', 'item__description', 'item__pk').annotate(count=Count("item__id")).order_by('-count')
    history_people = history.values('person__first_name', 'person__last_name', 'person__pk').annotate(count=Count("person")).order_by('-count')

    return render(request, 'checkout/reports.html', {'history': history, 'history_category': history_category, 'history_items': history_items, 'history_people': history_people, 'transactions': transactions, 'all_people': all_people, 'borrowers': borrowers, 'loaned_items': loaned_items, 'active_people': active_people, 'active_items': active_items})

def history(request):
    history = TransactionHistory.objects.all().order_by('-time_in')
    return render(request, 'checkout/history.html', {'history': history})

def person_list(request, tab='all'):
    if tab == 'reservations':
      people = Person.objects.filter(pk__in=[x for x in Transaction.objects.filter(time_out__isnull=False).values_list('person', flat=True)])
    elif tab == 'loans':
      people = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=True).values_list('person', flat=True)])
    else:
      people = Person.objects.all()

    return render(request, 'checkout/person_list.html', {'people': people, 'tab': tab})


def person_search(request):
    if request.method == "POST":
      #response = HttpResponse("You are searching for: " + request.POST.get('person', 'Bob'))
      #return response
      person = get_object_or_404(Person, id_number=request.POST.get('person', None))
      return person_detail(request, pk=person.pk)
    else:
	  return person_list(request)
    
def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    transactions = Transaction.objects.all()
    item = Transaction.objects.filter(person=pk).filter(time_out__isnull=False)
    requests = Transaction.objects.filter(person=pk).filter(time_out__isnull=True)
    available_items = Item.objects.exclude(pk__in = [x for x in Transaction.objects.values_list('item', flat=True)])

    categories = Category.objects.all().order_by('name')

    history = TransactionHistory.objects.filter(person=pk)
    return render(request, 'checkout/person_detail.html', {'categories': categories, 'person': person, 'item': item, 'requests': requests, 'available_items': available_items, 'history': history})

def person_history(request, pk):
    person = get_object_or_404(Person, pk=pk)
    transactions = Transaction.objects.all()
    history = TransactionHistory.objects.filter(person=pk)
    return render(request, 'checkout/person_history.html', {'person': person, 'history': history})

def requests(request):
    transactions = Transaction.objects.all()
    people = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=True).values_list('person', flat=True)])
    return render(request, 'checkout/requests.html', {'people': people})

def check_in(request):
    transactions = Transaction.objects.all()
    people = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=False).values_list('person', flat=True)])
    return render(request, 'checkout/check_in.html', {'people': people})
	
def item_search(request, pk):
    if request.method == "POST":
      #response = HttpResponse("You are searching for: " + request.POST.get('person', 'Bob'))
      #return response
      person = get_object_or_404(Person, pk=pk)
      item = get_object_or_404(Item, inventory_id=request.POST.get('item', None))
      return request_item(request, p=person.pk, i=item.pk)
    else:
	  return person_detail(request, pk)
	  
def item_checkin(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.check_in()
    return redirect('checkout.views.reservations')

def item_popup(request, pk):
    item = get_object_or_404(Item, pk=pk)
    transactions = Transaction.objects.all()
    history = TransactionHistory.objects.filter(item=pk)
    return render(request, 'checkout/item_popup.html', {'item': item, 'history': history})

def browse_items(request, pk):
    person = get_object_or_404(Person, pk=pk)
    transactions = Transaction.objects.all()
    available_items = Catalog.objects.exclude(pk__in = [x for x in Transaction.objects.values_list('item', flat=True)])
    categories = Category.objects.all().order_by('name')
    return render(request, 'checkout/browse_items.html', {'categories': categories, 'person': person, 'available_items': available_items})

def item_list(request):
    items = Item.objects.all().order_by('category')
    return render(request, 'checkout/item_list.html', {'items': items})

def request_item(request, p, i):
    person = get_object_or_404(Person, pk=p)
    item = get_object_or_404(Item, pk=i)
    try:
      transaction = Transaction.objects.get(item=item.pk)
    except Transaction.DoesNotExist:
    	transaction = Transaction.objects.create(person=person, item=item)
    return redirect('checkout.views.person_detail', pk=person.pk)

def quick_checkout(request, p):
    person = get_object_or_404(Person, pk=p)
    if request.method == "POST":
      item = get_object_or_404(Item, inventory_id=request.POST.get('item', None))
    try:
        transaction = Transaction.objects.get(item=item.pk)
    except Transaction.DoesNotExist:
    	transaction = Transaction.objects.create(person=person, item=item)
    transaction.check_out()
    return redirect('checkout.views.person_detail', pk=person.pk)

def person_cancel_request(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.cancel_request()
    return redirect('checkout.views.person_detail', pk=transaction.person.pk)

def cancel_request(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.cancel_request()
    return redirect('checkout.views.reservations')

def checkout_item(request, p, i):
    person = get_object_or_404(Person, pk=p)
    item = get_object_or_404(Item, pk=i)
    transaction = Transaction.objects.get(person=person, item=item)
    transaction.check_out()

    return redirect('checkout.views.reservations')
    
def delete_transaction(request, t):
    transaction = get_object_or_404(Transaction, pk=t)
    transaction.cancel_request()

    return redirect('checkout.views.reservations')