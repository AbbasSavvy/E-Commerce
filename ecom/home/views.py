from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from product.models import Category


def index(request):
    category = Category.objects.all()
    page = 'home'
    context = {'page': page, 'category': category}
    return render(request, 'index.html', context)
