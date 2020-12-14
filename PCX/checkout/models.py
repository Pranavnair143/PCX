from django.db import models

from django.contrib.auth.models import User

from django.forms import ModelForm
from product.models import product_full
from user.models import UserProfile

# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(product_full,on_delete=models.SET_NULL,null=True)
    qnty=models.IntegerField()
    
    @property
    def amount(self):
        return (self.qnty*self.product.p_rate)
    
    def __str__(self):
        return self.user.username

class cart_form(ModelForm):
    class Meta:
        model=Cart
        fields=['qnty']
        
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    code=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=10)
    district=models.CharField(max_length=10)
    state=models.CharField(max_length=10)
    create_at=models.DateTimeField(auto_now_add=True)
    total=models.IntegerField()
    
    def __str__(self):
        return self.code

class order_form(ModelForm):
    class Meta:
        model=Order
        fields=['address','city','district','state']
    
class OrderSummary(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product_full,on_delete=models.CASCADE)
    price=models.IntegerField()
    qnty=models.IntegerField()
    amount=models.IntegerField()
    
    def __str__(self):
        return self.product.p_name