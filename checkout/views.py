from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Count, F
from .models import Transaction, Person, Item, Category
from .forms import TransactionForm

def dashboard(request):
    open_transactions = Transaction.active_objects.all()
    active_people = Person.active_people.all()
    active_items = Item.active_items.all()
    return render(request, 'checkout/dashboard.html', {'open_transactions': open_transactions, 'active_people': active_people, 'active_items': active_items})

def person_list(request):
    people = Person.objects.all()
    return render(request, 'checkout/person_list.html', {'people': people})

def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    inventory = person.get_inventory()
    history = person.get_history()
    return render(request, 'checkout/person_detail.html', {'person': person, 'inventory': inventory, 'history': history})

def item_checkin(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.check_in()
    return redirect('checkout.views.person_detail', pk=transaction.person.pk)

def list_categories(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'checkout/category_list.html', {'categories': categories})

def category_list(request, pk):
    person = get_object_or_404(Person, pk=pk)
    categories = Category.objects.all().order_by('name')
    return render(request, 'checkout/list_categories.html', {'person': person, 'categories': categories})

def list_available_items(request, p, c):
    person = get_object_or_404(Person, pk=p)
    category = get_object_or_404(Category, pk=c)
    available_items = Item.available_items.filter(category=category)
    return render(request, 'checkout/item_list.html', {'person': person, 'category': category, 'items': available_items})

def item_checkout(request, p, c, i):
    person = get_object_or_404(Person, pk=p)
    item = get_object_or_404(Item, pk=i)
    transaction = Transaction.objects.create(person=person, item=item)
    transaction.check_out()
    return redirect('checkout.views.person_detail', pk=person.pk)

def transaction_new(request):
	if request.method == "POST":
		form = TransactionForm(request.POST)
		if form.is_valid():
			transaction = form.save(commit=False)
			transaction.time_out = timezone.now()
			transaction.save()
			return redirect('checkout.views.transaction_detail', pk=transaction.pk)
	else:
		form = TransactionForm()
	return render(request, 'checkout/transaction_edit.html', {'form': form})
