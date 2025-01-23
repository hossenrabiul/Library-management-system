from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type']

    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop('profile')
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True   # ei field disable thakbe
        self.fields['transaction_type'].widget = forms.HiddenInput()  # user er theke hide thakbe
    
    def save(self, commit = True):
        self.instance.profile = self.profile
        self.instance.balance_after_transactions = self.profile.amount
        return super().save()
    

class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 50
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You have to deposit at least {min_deposit_amount}$'
            )
        return amount