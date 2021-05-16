from django.contrib import admin

# Register your models here.
from cart.models import ShopCart

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','discountedprice','amount' ]
    list_filter = ['user']

admin.site.register(ShopCart,ShopCartAdmin)
