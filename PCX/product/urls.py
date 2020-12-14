from django.urls import path

from . import views

app_name='products'

urlpatterns = [
    path('submit_rev/<int:id>', views.submit_rev, name='submit_rev'),
    path('addon/<int:id>', views.add_to_wishlist, name='a_wlist'),
]