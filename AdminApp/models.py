from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=40)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.cat_name
    
    
class Furniture(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to = "Images")
    cat_fk = models.ForeignKey('Category', on_delete = models.CASCADE)

    class Meta:
        db_table = "Furniture"

class OwnerAccount(models.Model):
    Ownercardno = models.CharField(max_length=4)
    Ownercvv = models.CharField(max_length=4)
    balance = models.FloatField(default=0)

    class Meta:
        db_table = "OwnerAccount"



class OrderMaster(models.Model):
    user = models.ForeignKey("UserApp.UserInfo", on_delete=models.CASCADE)
    amount = models.FloatField()
    details = models.CharField(max_length=300)

    class Meta:
        db_table = "OrderMaster"

