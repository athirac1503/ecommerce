from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=28)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=30)
    mobile_number=models.BigIntegerField()
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=40)

    class Meta:
        db_table='customer'

class Reseller(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    address=models.CharField(max_length=30)
    mobile_number=models.BigIntegerField()
    adhar_num=models.BigIntegerField()
    bank_holder_name=models.CharField(max_length=30)
    account_number=models.BigIntegerField()
    ifsc_code=models.CharField(max_length=50)
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=40)
    
    class Meta:
        db_table='reseller'