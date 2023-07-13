from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class MyTable(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    contact_number = PhoneNumberField(region="CA",widget=PhoneNumberPrefixWidget(country_choices=[("CA", "Canada"),("FR", "France"),],),)
    client_name = models.CharField(max_length=20)
    vendor_name = models.CharField(max_length=20)
    vendor_company = models.CharField(max_length=20)
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    currency_choices = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
    ]
    currency = models.CharField(max_length=10, choices=currency_choices)
    contract_choices = [
        ('Remote', 'Remote'),
        ('On Site', 'On Site'),
        ('Hybrid', 'Hybrid'),
    ]
    contract_type = models.CharField(max_length=20, choices=contract_choices)
    status_choices = [
        ('On Board ', 'On Board'),
        ('In Progress', 'In Progress'),
        ('No Response', 'No Response'),
        ('Closed', 'Closed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices)
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.vendor_name
