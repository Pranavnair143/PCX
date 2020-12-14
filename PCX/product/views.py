from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import product_review_form,product_review,product_full
from wishlist.models import Wishlist

# Create your views here.

def submit_rev(request,id):
    url=request.META.get('HTTP_REFERER')
    if request.method=='POST':
        form=product_review_form(request.POST)
        if form.is_valid():
            data=product_review()
            data.cus_rev=request.POST['cus_rev']
            data.rate=request.POST['rate']
            data.product=product_full.objects.get(pk=id)
            current_user=request.user
            data.user_id=current_user.id
            data.save()
            messages.success(request,"Your review has ben sent. Thank you for your interest.")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

@login_required(login_url='login/')
def add_to_wishlist(request,id):
    url=request.META.get('HTTP_REFERER')
    check=Wishlist.objects.filter(product_id=id,user_id=request.user.id)
    if check:
        Wishlist.objects.filter(product_id=id,user_id=request.user.id).delete()
        messages.success(request,'Item removed from wishlist successfully..!!')
    else:
        data=Wishlist()
        data.user_id=request.user.id
        data.product_id=id
        data.save()
        messages.success(request,'Item added to wishlist successfully..!!')
    return HttpResponseRedirect(url)


def get_queryset(query=None,o='p_rate'):
    queryset=[]
    queries=query.split(" ")
    for q in queries:
        posts=product_full.objects.filter(
            Q(p_brand__icontains=q) |
            Q(p_name__icontains=q) |
            Q(typ__icontains=q)
        ).distinct()
        for post in posts:
            queryset.append(post)
    ql=list(set(queryset)).order_by(o)
    return ql
