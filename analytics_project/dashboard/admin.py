from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_category', 'payment_method', 'shipping_cost', 'unit_price')

admin.site.register(Order, OrderAdmin)