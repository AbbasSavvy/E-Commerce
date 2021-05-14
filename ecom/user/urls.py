from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('password/', views.user_password, name='user_password'),
    path('updateprofile/', views.user_update, name='index'),
    path('manageaddress/', views.user_addressupdate, name='index'),
    path('managecontact/', views.user_contactupdate, name='index'),

]