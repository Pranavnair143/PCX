from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models import Avg

class product_full(models.Model):
    p_types_list=[('Laptop','Laptop'),('Accessories','Accessories'),('Software','Software')]
    p_type=models.CharField(max_length=30,choices=p_types_list)
    p_brand=models.CharField(max_length=20)
    p_name=models.CharField(max_length=30)
    typ=models.CharField(max_length=30)
    screen_size=models.FloatField()
    screen_res=models.TextField()
    cpu=models.TextField()
    ram=models.IntegerField()
    memory=models.TextField()
    gpu=models.TextField()
    op_sys=models.TextField()
    weight=models.FloatField()
    p_rate=models.FloatField()
    
    def __str__(self):
        return self.p_name
    
    @property
    def int_rate(self):
        return str(self.p_rate).split('.')[0]
    
    @property
    def dec_rate(self):
        return str(str(self.p_rate).split('.')[1])[:2]
    
    def get_product_url(self):
        return reverse("core:product",kwargs={"pk":self.pk})
    
    def add_cart_product(self):
        return reverse("core:add_to_cart",kwargs={"pk":self.pk})
    
    def remove_product(self):
        return reverse("core:remove_product",kwargs={"pk":self.pk})
    
    @property
    def averagereview(self):
        reviews=product_review.objects.filter(product=self).aggregate(average=Avg('rate'))
        avg=0
        if reviews["average"] is not None:
            avg=float(reviews["average"])
        return avg

    def countreview(self):
        reviews=product_review.objects.filter(product=self).aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt=int(reviews["count"])
        return cnt
    
class product_review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rate=models.IntegerField(default=0)
    product=models.ForeignKey(product_full,on_delete=models.CASCADE)
    cus_rev=models.TextField()
    
    def __str__(self):
        return self.cus_rev
    
class product_review_form(ModelForm):
    class Meta:
        model=product_review
        fields=['rate','cus_rev']