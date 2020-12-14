from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect 
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

from product.views import get_queryset

from product.models import product_full,product_review
from wishlist.models import Wishlist


class home(TemplateView):
    template_name='main-bs.html'

def product_view(request,id):
    product=product_full.objects.get(pk=id)
    review=product_review.objects.filter(product_id=id)
    w_list=Wishlist.objects.filter(user_id=request.user.id,product_id=id)
    context={'product':product,'reviews':review,'w_list':w_list}
    return render(request,'prodpage-bs.html',context)

def product_search(request):
    context={}
    t=''
    if request.GET:
        query=request.GET.get('search_p',t)
        t=query
        context['query']=str(query)
    products=get_queryset(query)
    page=request.GET.get('page',1)
    context['page']=page
    products_paginator=Paginator(products,10)
    try:
        products=products_paginator.page(page)
    except PageNotAnInteger:
        products=products_paginator.page(10)
    except EmptyPage:
        products=products_paginator.page(products_paginator.num_pages)
    context['products']=products
    return render(request,"p_list.html", context)