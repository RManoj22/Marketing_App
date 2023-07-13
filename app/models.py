from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MyTable(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    contact_number = models.CharField(max_length=15)
    client_name = models.CharField(max_length=20)
    vendor_name = models.CharField(max_length=20)
    vendor_company = models.CharField(max_length=20)
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=10)
    contract_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.vendor_name
