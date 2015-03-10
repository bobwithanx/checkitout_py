from django import forms

from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('item', 'student', 'out_time', 'in_time')

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('item', 'student', 'out_time', 'in_time')

