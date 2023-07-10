from django import forms
from .models import MyTable

class MyTableForm(forms.ModelForm):
    class Meta:
        model = MyTable
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Date', 'type': 'date'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Phone Number'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Client Name'}),
            'vendor_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Vendor Name'}),
            'vendor_company': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Vendor Company'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Rate'}),
            'contract_type': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Contract Type'}),
            'status': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Status'}),
        }
