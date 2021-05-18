from django.contrib import admin

# Register your models here.
from cart.models import *

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','discountedprice','amount' ]
    list_filter = ['user']

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product','price','quantity','amount')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','phone','city','total','status']
    list_filter = ['status']
    readonly_fields = ('user','delivery_type','address','city','country','pin_code','state','paymentmethod','phone','first_name','ip', 'last_name','phone','city','total')
    can_delete = False
    inlines = [OrderProductline]

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','price','quantity','amount']
    list_filter = ['user']

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)
admin.site.register(ShopCart,ShopCartAdmin)
