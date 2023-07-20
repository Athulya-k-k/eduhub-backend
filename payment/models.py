from django.db import models
from base.models import User

# Create your models here.

class Order(models.Model):
    order_payment_id = models.CharField(max_length=100)
    order_user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_amount = models.CharField(max_length=25)
    isPaid = models.BooleanField(default=False)
    order_date = models.DateField(auto_now=False)
    firtname = models.CharField(max_length=500,null=False)
    # lastname = models.CharField(max_length=500,null=False)
    # addrress1 = models.CharField(max_length=500,null=False)
    # addrress2 = models.CharField(max_length=500,null=False)
    # email = models.CharField(max_length=500,null=False)
    # phone = models.CharField(max_length=500,null=False)
   
  

    def __str__(self):
        return self.order_payment_id