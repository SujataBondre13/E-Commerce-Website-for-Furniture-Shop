from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    userCardNo = models.CharField(default = 0000, max_length=4)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=10)

    class Meta:
        db_table = "UserInfo"

class MyCart(models.Model):
    user = models.ForeignKey('UserInfo', on_delete= models.CASCADE)
    furniture = models.ForeignKey('AdminApp.Furniture', on_delete= models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = "MyCart"


class Shipping_Details(models.Model):
    customer_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()

    class Meta:
        db_table = "Shipping_Details"