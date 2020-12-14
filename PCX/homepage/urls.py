from django.urls import path,include
from .views import product_search,home

app_name='product'

urlpatterns = [
    path('',home.as_view(),name='main'),
    path('search/',product_search,name='search'),
    
]