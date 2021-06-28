import django_filters
from django_filters import filters,widgets
from django.forms import TextInput
from django.db import models
from django.db.models import Q
from functools import reduce
from django_property_filter import PropertyFilterSet,PropertyOrderingFilter
#from django.contrib.postgres.fields import IntegerRangeField

from product.models import product_full


class p_filter(django_filters.FilterSet):
    #search=filters.CharFilter(method='lookup_mtd')
    #price=django_filters.CharFilter(,widget=widgets.RangeWidget(attrs={})
    #price__gt = django_filters.NumberFilter(field_name='p_rate', lookup_expr='gt')
    #price__gt = django_filters.CharFilter(method='gt')
    #price__lt = django_filters.CharFilter(method='lt')
    #price__lt = django_filters.NumberFilter(field_name='p_rate', lookup_expr='lt')
    order=filters.OrderingFilter(fields=['p_rate'],widget=widgets.LinkWidget)
    """
    class Meta:
        model=product_full
        fields=['price__gt','price_lt']
    def gt(self,queryset,name,value):
        return queryset.filter(p_rate__gt=value)

    def lt(self,queryset,name,value):
        return queryset.filter(p_rate__lt=value)
"""
class property_filter(PropertyFilterSet):
    order=PropertyOrderingFilter(fields=('averagereview','averagereview'),widget=widgets.LinkWidget)
    class Meta:
        model=product_full
        fields=['order']