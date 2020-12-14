from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from .serializers import product_serializer
from product.models import product_full

class ApiListView(ListAPIView):
    serializer_class=product_serializer
    pagination_class=PageNumberPagination
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['p_name','p_brand','typ']
    ordering_fields=['p_rate','averagereview']

"""
    def get_queryset(self,*args,**kwargs):
        queryset=product_full.objects.all()
        query=self.request.GET.get('search_p')
        ordering=self.request.GET.get('o','p_rate')
        if query:
            queries=query.split(" ")
            for q in queries:
                posts=product_full.objects.filter(
                    Q(p_brand__icontains=q) |
                    Q(p_name__icontains=q) |
                    Q(typ__icontains=q)
                ).distinct()
                for post in posts:
                    queryset.append(post)
        return list(set(queryset)).order_by(ordering)
"""