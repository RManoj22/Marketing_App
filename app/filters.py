import django_filters
from django import forms
from .models import MyTable

class FormFilter(django_filters.FilterSet):

    class Meta:
         model = MyTable
         fields = ['status','currency','user']