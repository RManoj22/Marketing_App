from django import forms
from .models import MyTable
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class MyTableForm(forms.ModelForm):
    class Meta:
        model = MyTable
        fields = '__all__'
        widgets = {
            'contact_number': PhoneNumberField(widget=PhoneNumberPrefixWidget),
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'vendor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Name'}),
            'vendor_company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Company'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rate'}),
            'currency': forms.Select(choices=MyTable.currency_choices, attrs={'class':'form-control', 'placeholder': 'Currency'}),
            'contract_type': forms.Select(choices=MyTable.contract_choices, attrs={'class':'form-control', 'placeholder': 'Contract Type'}),
            'status': forms.Select(choices=MyTable.status_choices, attrs={'class': 'form-control', 'placeholder': 'Status'}),
            'comments': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comments'}),
        }
