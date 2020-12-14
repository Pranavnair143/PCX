from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.utils.crypto import get_random_string
from .models import Cart,cart_form,Order,order_form,OrderSummary
from product.models import product_full
from user.models import UserProfile

# Create your views here.

@login_required(login_url='login/')
def add_to_cart(request,id):
    url=request.META.get('HTTP_REFERER')
    current_user=request.user
    product=product_full.objects.get(pk=id)
    p_in_cart=Cart.objects.filter(user_id=current_user.id,product_id=id)
    if p_in_cart:
        count=1
    else:
        count=0
    if request.method=='POST':
        form=cart_form(request.POST)
        if form.is_valid():
            if count:
                data=Cart.objects.get(user_id=current_user.id,product_id=id)
                data.qnty+=form.cleaned_data['qnty']
                data.save()
            else:
                data=Cart()
                data.user_id=current_user.id
                data.product_id=id
                data.qnty=form.cleaned_data['qnty']
                data.save()
        messages.success(request,'Your item is added to cart..!!!')
        return HttpResponseRedirect(url)
    else:
        if count:
            data=Cart.objects.get(user_id=current_user.id,product_id=id)
            data.qnty+=1
            data.save()
        else:
            data=Cart()
            data.user_id=current_user.id
            data.product_id=id
            data.qnty=1
            data.save()
        messages.success(request,'Your item is added to cart..!!!')
        return HttpResponseRedirect(url)
    
def cart(request):
    current_user=request.user
    cart=Cart.objects.filter(user_id=current_user.id)
    total=0
    for i in cart:
        total+=i.qnty*i.product.p_rate
    context={'cart':cart,'total':total}
    return render(request,'cart.html',context)

@login_required(login_url='login/')
def remove_from_cart(request,id):
    Cart.objects.filter(id=id).delete()
    messages.success(request,'Item removed from cart successfully..!!!')
    return HttpResponseRedirect('/cart')

def order_cart(request):
    cart=Cart.objects.filter(user_id=request.user.id)
    total=0
    for i in cart:
        total+=i.qnty*i.product.p_rate
    profile_info=UserProfile.objects.filter(user_id=request.user.id)
    if request.method=='POST':
        if profile_info:
            form=order_form(request.POST)
            if form.is_valid():
                data=Order()
                data.user_id=request.user.id
                o_code=get_random_string(10).upper()
                data.code=o_code
                data.address=form.cleaned_data['address']
                data.city=form.cleaned_data['city']
                data.district=form.cleaned_data['district']
                data.state=form.cleaned_data['state']
                data.total=total
                #data.payment_type=request.POST('p_type')
                data.save()

                for i in cart:
                    os=OrderSummary()
                    os.order_id=data.id
                    os.user_id=request.user.id
                    os.product_id=i.product_id
                    os.price=i.product.p_rate
                    os.qnty=i.qnty
                    os.amount=i.amount
                    os.save()
                Cart.objects.filter(user_id=request.user.id).delete()
                o_sum=OrderSummary.objects.filter(order_id=data.id)
                context={'o_sum':o_sum,'total':total,'o_code':o_code}
                return render(request,'order_summary.html',context)
            else:
                messages.warning(request,form.errors)
                return HttpResponseRedirect('/checkout/order')
        else:
            return HttpResponseRedirect('/user/update_p')
    form=order_form()
    if profile_info:
        u_profile=UserProfile.objects.get(user_id=request.user.id)
    else:
        return HttpResponseRedirect('/user/update_p')
    context={'u_profile':u_profile,'form':form,'total':total,'cart':cart}
    return render(request,'order_form.html',context)