import django_filters
from django import forms
from .models import MyTable

class FormFilter(django_filters.FilterSet):

    # currency = django_filters.CharFilter(field_name='currency',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Currency'}))
    # status = django_filters.CharFilter(field_name='status',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status'}))

    class Meta:
         model = MyTable
         fields = ['status','currency']