from django.db import models

# Create your models here.
class User(models.Model):
    uid=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=100)
    uemail=models.EmailField(max_length=100)
    uphone=models.BigIntegerField()
    upassword=models.CharField(max_length=100)

class Event(models.Model):
    eid=models.AutoField(primary_key=True)
    etitle=models.CharField(max_length=100)
    edesc=models.CharField(max_length=100)
    ecity=models.CharField(max_length=100)
    elocation=models.CharField(max_length=100)
    edate=models.DateField()
    etime=models.TimeField()
    vticket=models.IntegerField()
    gticket=models.IntegerField()

class Booking(models.Model):
    bid=models.AutoField(primary_key=True)
    eid=models.ForeignKey(Event,default=None,on_delete=models.CASCADE)
    uid=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    bdate=models.DateField(auto_now=True)
    ttype=models.CharField(max_length=20,default=None)
    quantity=models.IntegerField()

class owner(models.Model):
    oid=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

class Payment(models.Model):
    pid = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)


    