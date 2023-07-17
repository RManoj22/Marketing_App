from django import forms
from .models import MyTable
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'password1']

class MyTableForm(forms.ModelForm):

    # contact_number = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}))

    class Meta:
        model = MyTable
        fields = '__all__'
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'vendor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Name'}),
            'vendor_company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Company'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rate'}),
            'currency': forms.Select(choices=MyTable.currency_choices, attrs={'class':'form-control', 'placeholder': 'Currency'}),
            'contract_type': forms.Select(choices=MyTable.contract_choices, attrs={'class':'form-control', 'placeholder': 'Contract Type'}),
            'status': forms.Select(choices=MyTable.status_choices, attrs={'class': 'form-control', 'placeholder': 'Status'}),
            'comments': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comments'}),
        }
