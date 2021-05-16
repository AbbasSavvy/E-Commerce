from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import get_random_string

from cart.models import ShopCart, ShopCartForm
from product.models import Category, Product
from user.models import User1Profile, User2Profile

@login_required(login_url='/login') # Check login
def addtoshopcart(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    product= Product.objects.get(pk=id)

    checkinproduct = ShopCart.objects.filter(product_id=id, user_id=current_user.id) # Check product in shopcart
    if checkinproduct:
        control = 1
    else:
        control = 0

    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control==1: # Update  shopcart
                data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
                quantity_desired= data.quantity +form.cleaned_data['quantity']
                leftover= product.product_stock-quantity_desired
                if leftover>=0:
                    data.quantity += form.cleaned_data['quantity']
                    data.save()  # save data
                    messages.success(request, "Product added to Shopcart ")
                else:
                    messages.info(request, "Out of Stock. Decrease your quantity and try.")
            else: # Insert to Shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                leftover = product.product_stock - form.cleaned_data['quantity']
                if leftover>=0:
                    data.quantity = form.cleaned_data['quantity']
                    data.save()
                    messages.success(request, "Product added to Shopcart ")
                else:
                    messages.info(request, "Out of Stock. Decrease your quantity and try.")

        return HttpResponseRedirect(url)

    else: # if there is no post
        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            quantity_desired = data.quantity + 1
            leftover = product.product_stock - quantity_desired
            if leftover >= 0:
                data.quantity += 1
                data.save()
                messages.success(request, "1 item added to Shopcart ")
            else:
                messages.info(request, "Out of stock. Cannot add item")
        else:  #  Inser to Shopcart
            data = ShopCart()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            leftover = product.product_stock - 1
            if leftover >= 0:
                data.quantity = 1
                data.save()  #
                messages.success(request, "Product added to Shopcart ")
            else:
                messages.info(request, "Out of Stock.")
        return HttpResponseRedirect(url)

def shopcart(request):
    category = Category.objects.all()
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for rs in shopcart:
        total += rs.product.product_discount * rs.quantity
    #return HttpResponse(str(total))
    context={'shopcart': shopcart,
             'category':category,
             'total': total,
             }
    return render(request,'shopcart_products.html',context)

@login_required(login_url='/login') # Check login
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted form Shopcart.")
    return HttpResponseRedirect("/shopcart")

@login_required(login_url='/login') # Check login
def addproduct(request,id):
    current_user = request.user  # Access User Session information
    product= Product.objects.get(pk=id)
    data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
    data.quantity += 1
    data.save()  #

    messages.success(request, "Product added to Shopcart")
    return HttpResponseRedirect("/shopcart")

@login_required(login_url='/login') # Check login
def reduceproduct(request,id1,id2):
    current_user = request.user  # Access User Session information
    product= Product.objects.get(pk=id1)
    data = ShopCart.objects.get(product_id=id1, user_id=current_user.id)
    data.quantity -= 1
    data.save()
    if data.quantity==0:
        ShopCart.objects.filter(id=id2).delete()
        messages.success(request, "Your item deleted form Shopcart.")
    else:
        messages.success(request, "Product reduced from Shopcart")
    return HttpResponseRedirect("/shopcart")
