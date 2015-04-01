from django import forms

from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('item', 'person', 'time_out')

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('item', 'person', 'time_out')

