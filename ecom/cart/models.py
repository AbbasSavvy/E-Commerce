from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm
from product.models import Product

class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.product_name

    @property
    def discountedprice(self):
        return (self.product.product_discount)

    @property
    def amount(self):
        return (self.quantity * self.product.product_discount)

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
