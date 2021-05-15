from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from product.models import Category, Product, Images


def index(request):
    category = Category.objects.all()
    sliderProducts = Product.objects.all().order_by('id')[:4]
    latestProducts = Product.objects.all().order_by('-id')[:4]
    randomProducts = Product.objects.all().order_by('?')[:2]
    page = 'home'
    context = {'page': page,
               'category': category,
               'sliderProducts': sliderProducts,
               'latestProducts':latestProducts,
               'randomProducts':randomProducts}
    return render(request, 'index.html', context)


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    context = {'category': category,
               'product': product,
               'images':images,
               }
    return render(request, 'product_detail.html', context)

def category_products(request, id, slug):
    catdata = Category.objects.get(pk=id)
    category = Category.objects.all()
    products = Product.objects.filter(category=id)
    context = {'category': category,
               'catdata': catdata,
               'product':products,
               }
    # return HttpResponse(products)
    return render(request, 'category_products.html', context)