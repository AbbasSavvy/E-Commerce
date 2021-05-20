from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import query
from django.http.response import HttpResponseRedirect
from home.forms import SearchForm
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from product.models import Category, Product, Images


def index(request):
    category = Category.objects.all()
    sliderProducts = Product.objects.all().order_by('id')[:4]
    latestProducts = Product.objects.all().order_by('-id')[:4]
    randomProducts = Product.objects.all().order_by('?')[:4]
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
    all_prods = Product.objects.filter(category=id)
    if all_prods.count()>0:
        page = request.GET.get('page', 1)
        paginator = Paginator(all_prods, 2)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    else:
        products = Product.objects.filter(category=id)
    context = {'category': category,
               'catdata': catdata,
               'product':products,
               }
    # return HttpResponse(products)
    return render(request, 'category_products.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']

            if catid == 0:
                products = Product.objects.filter(product_name__icontains=query)
            else:
                products = Product.objects.filter(product_name__icontains=query, category=catid)

            category = Category.objects.all()
            context = {
                'products': products,
                'category': category,}

            return render(request, 'search_product.html', context)
        
    return HttpResponseRedirect('/')
                    