from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('addproduct/<int:id>', views.addproduct, name='addproduct'),
    path('reduceproduct/<int:id1>/<int:id2>', views.reduceproduct, name='reduceproduct'),
]