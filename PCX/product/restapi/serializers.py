from rest_framework import serializers

from product.models import product_full

class product_serializer(serializers.ModelSerializer):
    class Meta:
        model=product_full
        fields=['p_rate','p_name','p_brand','ram']