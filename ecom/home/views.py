from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from product.models import Category, Product


def index(request):
    category = Category.objects.all()
    sliderProducts = Product.objects.all()
    page = 'home'
    context = {'page': page,
               'category': category,
               'sliderProducts': sliderProducts}
    return render(request, 'index.html', context)
