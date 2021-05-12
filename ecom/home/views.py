from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    name = 'Sarvesh'
    surname = 'Agrawal'
    context = {'name': name, 'surname': surname}
    return render(request, 'index.html', context)
