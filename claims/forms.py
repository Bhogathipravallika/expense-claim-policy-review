from django import forms
from .models import ExpenseClaim


class ExpenseClaimForm(forms.ModelForm):

    class Meta:
        model = ExpenseClaim

        fields = [
            'claimant',
            'date',
            'category',
            'amount',
            'currency',
            'description',
            'receipt_available',
        ]

        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }