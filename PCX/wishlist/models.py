from django.db import models
from django.contrib.auth.models import User

from product.models import product_full

# Create your models here.

class Wishlist(models.Model):
    product=models.ForeignKey(product_full,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.first_name