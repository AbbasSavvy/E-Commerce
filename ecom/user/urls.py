from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('password/', views.user_password, name='user_password'),
    path('updateprofile/', views.user_update, name='updateprofile'),
    path('manageaddress/', views.user_addressupdate, name='user_addressupdate'),
    path('managecontact/', views.user_contactupdate, name='user_contactupdate'),
    path('orders/', views.user_orders, name='user_orders'),
    path('orders_product/', views.user_order_product, name='user_order_product'),
    path('orderdetail/<int:id>', views.user_orderdetail, name='user_orderdetail'),
]