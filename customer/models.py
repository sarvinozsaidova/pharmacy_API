from django.db import models

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    contact_add = models.CharField(max_length=100)
    cust_email = models.CharField(max_length=100)
    cust_pass = models.CharField(max_length=100)

class Pharmacy(models.Model):
    phar_ID = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    contact_add = models.CharField(max_length=100)
    admin_email = models.CharField(max_length=100)
    admin_pass = models.CharField(max_length=100)

class Medicines(models.Model):
    med_ID = models.IntegerField(primary_key=True)
    med_category = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()

class Purchasing(models.Model):
    purchase_ID = models.IntegerField(primary_key=True)
    cust_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    med_ID = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateTimeField()
    items = models.IntegerField()

class Sales(models.Model):
    sales_ID = models.IntegerField(primary_key=True)
    phar_ID = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    cust_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    med_ID = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    count = models.BigIntegerField()
    purchase_ID = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    date = models.DateTimeField()
    total_amount = models.BigIntegerField()


class Reports(models.Model):
    report_ID = models.IntegerField(primary_key=True)
    purchase_ID = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    sales_ID = models.ForeignKey(Sales, on_delete=models.CASCADE)
    cust_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
