from django.db import models



class MyTable(models.Model):
    date = models.DateField()
    phone_number = models.IntegerField()
    client_name = models.CharField(max_length=20)
    vendor_name = models.CharField(max_length=20)
    vendor_company = models.CharField(max_length=20)
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    contract_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20)