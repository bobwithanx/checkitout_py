from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Count 
from .models import Transaction, Student, Item, Category
from .forms import TransactionForm

def dashboard(request):
  open_transactions = Transaction.with_inventory.all()
  assigned_equipment = Item.assigned_items.all()
  students = Student.objects.all()
  return render(request, 'checkout/dashboard.html', {'open_transactions': open_transactions, 'students': students, 'items': assigned_equipment})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'checkout/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    transactions = Transaction.objects.filter(student=student).exclude(in_time__isnull=False)
    return render(request, 'checkout/student_detail.html', {'student': student, 'transactions': transactions})

def item_checkin(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.in_time = timezone.now()
    transaction.save()
    transaction.item.assigned_to = None
    transaction.item.save()
    return redirect('checkout.views.student_detail', pk=transaction.student.pk)

def list_categories(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'checkout/category_list.html', {'categories': categories})

def category_list(request, pk):
    student = get_object_or_404(Student, pk=pk)
    categories = Category.objects.all().order_by('name')
    return render(request, 'checkout/list_categories.html', {'student': student, 'categories': categories})

def list_available_items(request, s, c):
    student = get_object_or_404(Student, pk=s)
    category = get_object_or_404(Category, pk=c)
    available_items = Item.objects.filter(category=category).filter(assigned_to__isnull=True)
    return render(request, 'checkout/item_list.html', {'student': student, 'category': category, 'items': available_items})

def item_checkout(request, s, c, i):
    	  student = get_object_or_404(Student, pk=s)
    	  item = get_object_or_404(Item, pk=i)
       	  transaction = Transaction.objects.create(item=item, student=student, out_time=timezone.now())
	  item.assigned_to = student
	  item.save()
	  transaction.save()
	  return redirect('checkout.views.student_detail', pk=student.pk)

def transaction_new(request):
    if request.method == "POST":
       form = TransactionForm(request.POST)
       if form.is_valid():
	  transaction = form.save(commit=False)
	  transaction.out_time = timezone.now()
	  transaction.save()
	  return redirect('checkout.views.transaction_detail', pk=transaction.pk)
    else:
       form = TransactionForm()
    return render(request, 'checkout/transaction_edit.html', {'form': form})
