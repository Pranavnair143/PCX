from django.urls import path

from . import views

urlpatterns = [
    path('addtocart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>', views.remove_from_cart, name='remove_from_cart'),
    path('order/', views.order_cart, name='order_cart'),
]