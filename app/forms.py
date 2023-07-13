from django import forms
from .models import MyTable
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

currency_choices = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
    ]
contract_choices = [
        ('Remote', 'Remote'),
        ('On Site', 'On Site'),
        ('Hybrid', 'Hybrid'),
    ]

status_choices = [
        ('On Board ', 'On Board'),
        ('In Progress', 'In Progress'),
        ('No Response', 'No Response'),
        ('Closed', 'Closed'),
    ]

class MyTableForm(forms.ModelForm):

    # contact_number = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}))

    class Meta:
        model = MyTable
        fields = '__all__'
        widgets = {
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'vendor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Name'}),
            'vendor_company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Company'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rate'}),
            'currency': forms.Select(choices=currency_choices, attrs={'class':'form-control', 'placeholder': 'Currency'}),
            'contract_type': forms.Select(choices=contract_choices, attrs={'class':'form-control', 'placeholder': 'Contract Type'}),
            'status': forms.Select(choices=status_choices, attrs={'class': 'form-control', 'placeholder': 'Status'}),
            'comments': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comments'}),
        }
