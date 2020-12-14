"""PCX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from homepage import views as homeviews
from user import views as userviews
from checkout import views as chkviews
from wishlist import views as w_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls')),
    path('user/',include('user.urls')),
    path('checkout/',include('checkout.urls')),
    path('product/',include('product.urls')),
    path('product/<int:id>',homeviews.product_view,name='product_full'),
    path('user/accounts/',include('allauth.urls')),
    path('login/',userviews.login_form,name='login'),
    path('signup/',userviews.signup_form,name='signup'),
    path('logout/',userviews.log_out,name='logout'),
    path('cart/',chkviews.cart, name='show_cart'),
    path('w_list/',w_views.view_wishlist, name='show_wishlist'),
    path('restapi/product/', include('product.restapi.urls','products_api')),
    path('search/',homeviews.product_search,name='search'),
]