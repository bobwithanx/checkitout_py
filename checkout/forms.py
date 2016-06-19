from django import forms

from .models import Transaction, Item, Person

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('item', 'person', 'time_out')

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('item', 'person', 'time_out')

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'display_name', 'image_name', 'serial', 'inventory_tag')

        
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'id_number', 'graduation_year', 'active')