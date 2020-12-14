from django.urls import path
from .views import ApiListView

app_name='products'

urlpatterns=[
    path('list',ApiListView.as_view(),name='list'),
]