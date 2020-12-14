from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=10)
    district=models.CharField(max_length=10)
    state=models.CharField(max_length=10)
    
    def __str__(self):
        return self.user.username
    
    def __username__(self):
        return self.user.first_name+' '+self.user.last_name