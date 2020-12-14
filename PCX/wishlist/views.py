from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Wishlist

# Create your views here.

@login_required(login_url='login/')
def view_wishlist(request):
    w_list=Wishlist.objects.filter(user_id=request.user.id)
    context={'w_list':w_list}
    return render(request,'wishlist.html',context)