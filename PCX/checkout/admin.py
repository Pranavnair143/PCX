from django.contrib import admin
from checkout.models import Cart,Order,OrderSummary

class CartAdmin(admin.ModelAdmin):
    list_display=['user','product','qnty']
    list_filter=['user']

class OrderProductline(admin.TabularInline):
    model = OrderSummary
    readonly_fields=('user', 'product','price','qnty','amount')
    can_delete=False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display=['user','code','total','create_at']
    list_filter=['user']
    readonly_fields=('user','code','address','city','district','state','total','create_at')
    can_delete=False
    inlines=[OrderProductline]

class OrderSummaryAdmin(admin.ModelAdmin):
    list_display=['user', 'product','price','qnty','amount']
    list_filter=['user']

# Register your models here.

admin.site.register(Cart,CartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderSummary,OrderSummaryAdmin)