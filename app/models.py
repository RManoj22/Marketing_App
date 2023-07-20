from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class MyTable(models.Model):
    # The line `user = models.ForeignKey(User, on_delete=models.CASCADE)` is creating a foreign key
    # relationship between the `MyTable` model and the built-in `User` model provided by Django's
    # authentication system.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # The `contact_number_validator` is a regular expression validator that is used to validate the
    # `contact_number` field in the `MyTable` model.
    contact_number_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Contact number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact_number = models.CharField(validators=[contact_number_validator],max_length=15)
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
            ('On Board', 'On Board'),
            ('In Progress', 'In Progress'),
            ('No Response', 'No Response'),
            ('Closed', 'Closed'),
        ]
    status = models.CharField(max_length=20, choices=status_choices)
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.vendor_name
