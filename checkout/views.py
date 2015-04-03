from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Count, F
from .models import Transaction, TransactionHistory, Person, Item, Category
from .forms import TransactionForm
from django.http import HttpRequest, HttpResponse

def dashboard(request):
    transactions = Transaction.objects.all()
    all_people = Person.objects.all()
    active_people = Person.objects.filter(pk__in=transactions)
    reservations = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=True).values_list('person', flat=True)])
    active_items = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=False).values_list('person', flat=True)])

    return render(request, 'checkout/dashboard.html', {'transactions': transactions, 'all_people': all_people, 'active_people': active_people, 'active_items': active_items, 'reservations': reservations})

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
    history_items = history.values('item__brand__name', 'item__model', 'item__serial', 'item__description').annotate(count=Count("item__id")).order_by('-count')
    history_people = history.values('person__first_name', 'person__last_name').annotate(count=Count("person")).order_by('-count')

    return render(request, 'checkout/reports.html', {'history': history, 'history_category': history_category, 'history_items': history_items, 'history_people': history_people, 'transactions': transactions, 'all_people': all_people, 'borrowers': borrowers, 'loaned_items': loaned_items, 'active_people': active_people, 'active_items': active_items})

def history(request):
    history = TransactionHistory.objects.all().order_by('-time_in')
    return render(request, 'checkout/history.html', {'history': history})

def person_list(request):
    people = Person.objects.all()
    return render(request, 'checkout/person_list.html', {'people': people})

def person_search(request):
    if request.method == "POST":
      
      #response = HttpResponse("You are searching for: " + request.POST.get('person', 'Bob'))
      #return response
      person = get_object_or_404(Person, id_number=request.POST.get('person', None))
      return person_detail(request, pk=person.pk)
    else:
	  return person_list(request)
    
def person_popup(request, pk):
    person = get_object_or_404(Person, pk=pk)
    transactions = Transaction.objects.all()
    inventory = Transaction.objects.filter(person=pk).filter(time_out__isnull=False)
    reservations = Transaction.objects.filter(person=pk).filter(time_out__isnull=True)
    available_items = Item.objects.exclude(pk__in = [x for x in Transaction.objects.values_list('item', flat=True)])
    history = TransactionHistory.objects.filter(person=pk)
    return render(request, 'checkout/person_popup.html', {'person': person, 'inventory': inventory, 'reservations': reservations, 'available_items': available_items, 'history': history})

def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    transactions = Transaction.objects.all()
    inventory = Transaction.objects.filter(person=pk).filter(time_out__isnull=False)
    reservations = Transaction.objects.filter(person=pk).filter(time_out__isnull=True)
    available_items = Item.objects.exclude(pk__in = [x for x in Transaction.objects.values_list('item', flat=True)])
    history = TransactionHistory.objects.filter(person=pk)
    return render(request, 'checkout/person_detail.html', {'person': person, 'inventory': inventory, 'reservations': reservations, 'available_items': available_items, 'history': history})

def person_history(request, pk):
    person = get_object_or_404(Person, pk=pk)
    transactions = Transaction.objects.all()
    history = TransactionHistory.objects.filter(person=pk)
    return render(request, 'checkout/person_history.html', {'person': person, 'history': history})

def reservations(request):
    transactions = Transaction.objects.all()
    people = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=True).values_list('person', flat=True)])
    return render(request, 'checkout/reservations.html', {'people': people})

def check_in(request):
    transactions = Transaction.objects.all()
    people = Person.objects.filter(pk__in = [x for x in Transaction.objects.filter(time_out__isnull=False).values_list('person', flat=True)])
    return render(request, 'checkout/check_in.html', {'people': people})
	

def item_search(request, pk):
    if request.method == "POST":
      #response = HttpResponse("You are searching for: " + request.POST.get('person', 'Bob'))
      #return response
      person = get_object_or_404(Person, pk=pk)
      item = get_object_or_404(Item, barcode_id=request.POST.get('item', None))
      return reserve_item(request, p=person.pk, i=item.pk)
    else:
	  return person_detail(request, pk)
	  
def item_checkin(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.check_in()
    return redirect('checkout.views.check_in')

def item_popup(request, pk):
    item = get_object_or_404(Item, pk=pk)
    transactions = Transaction.objects.all()
    history = TransactionHistory.objects.filter(item=pk)
    return render(request, 'checkout/item_popup.html', {'item': item, 'history': history})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    transactions = Transaction.objects.all()
    history = TransactionHistory.objects.filter(item=pk)
    return render(request, 'checkout/item_detail.html', {'item': item, 'history': history})

def item_list(request):
    items = Item.objects.all().order_by('category')
    return render(request, 'checkout/item_list.html', {'items': items})

def list_available_items(request, p, c):
    person = get_object_or_404(Person, pk=p)
    category = get_object_or_404(Category, pk=c)
    available_items = Item.available_items.filter(category=category)
    return render(request, 'checkout/item_list.html', {'person': person, 'category': category, 'items': available_items})

def reserve_item(request, p, i):
    person = get_object_or_404(Person, pk=p)
    item = get_object_or_404(Item, pk=i)
    try:
        transaction = Transaction.objects.get(item=item.pk)
    except Transaction.DoesNotExist:
    	transaction = Transaction.objects.create(person=person, item=item)
    return redirect('checkout.views.person_detail', pk=person.pk)

def person_cancel_reservation(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.cancel_reservation()
    return redirect('checkout.views.person_detail', pk=transaction.person.pk)

def cancel_reservation(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.cancel_reservation()
    return redirect('checkout.views.reservations')

def checkout_item(request, p, i):
    person = get_object_or_404(Person, pk=p)
    item = get_object_or_404(Item, pk=i)
    transaction = Transaction.objects.get(person=person, item=item)
    transaction.check_out()

    return redirect('checkout.views.reservations')