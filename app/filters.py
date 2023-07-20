import django_filters
from .models import MyTable

# The `FormFilter` class is a Django filter class that filters instances of the `MyTable` model based
# on the `status`, `currency`, and `user` fields.

class FormFilter(django_filters.FilterSet):

    class Meta:
         model = MyTable
         fields = ['status','currency','user']