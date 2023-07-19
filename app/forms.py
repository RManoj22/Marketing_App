from django import forms
from .models import MyTable
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput)      


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            }
 

class MyTableForm(forms.ModelForm):

    class Meta:
        model = MyTable
        fields = ['client_name', 'contact_number', 'vendor_name', 'vendor_company', 'rate', 'currency', 'contract_type', 'status', 'comments']
        exclude = ['user']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'contact_number': forms.TextInput(attrs={'id': 'contactForm','class': 'form-control', 'placeholder': 'Contact Number'}),
            'vendor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Name'}),
            'vendor_company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Company'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rate'}),
            'currency': forms.Select(choices=MyTable.currency_choices, attrs={'class':'form-control', 'placeholder': 'Currency'}),
            'contract_type': forms.Select(choices=MyTable.contract_choices, attrs={'class':'form-control', 'placeholder': 'Contract Type'}),
            'status': forms.Select(choices=MyTable.status_choices, attrs={'class': 'form-control', 'placeholder': 'Status'}),
            'comments': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comments'}),
        }
