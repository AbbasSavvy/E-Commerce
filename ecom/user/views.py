from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic.list import ListView
from django.forms import inlineformset_factory

from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db import transaction

# Create your views here.
from django.utils import translation
from product.models import Category
from user.models import User, User1Profile, User2Profile


@login_required(login_url='/login')
def index(request):
    category = Category.objects.all()
    current_user = request.user  # Access User Session information
    ty=current_user.id
    profile1 = User1Profile.objects.filter(user_id=ty)
    profile2 = User2Profile.objects.filter(user_id=ty)
    context = {'category': category,
               'profile1': profile1,
               'profile2': profile2}
    return render(request,'user_profile.html', context)

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.warning(request,"Login Error! Username or Password is incorrect")
            return HttpResponseRedirect('/login')


    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'login_form.html', context)

def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')

def newsignup(request):
    if request.method == 'POST':
        form = SignUp1Form(request.POST)
        form1 = SignUp2Form(request.POST)
        form2 = SignUp3Form(request.POST)
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            form.save()
            ok1 = form1.save(False)
            ok2 = form2.save(False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            ok1.user_id = current_user.id
            ok1.save()
            ok2.user_id = current_user.id
            ok2.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            messages.warning(request, form1.errors)
            messages.warning(request, form2.errors)
            return HttpResponseRedirect('/signup')


    form = SignUp1Form()
    form1 = SignUp2Form()
    form2 = SignUp3Form()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               'form1': form1,
               'form2': form2
               }
    return render(request, 'signup_form.html', context)

@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        context = {
            'category': category,
            'user_form': user_form,
        }
        return render(request, 'user_update.html', context)

@login_required(login_url='/login')
def user_addressupdate(request):
    current_user = request.user  # Access User Session information
    ty = current_user.id
    pare=User.objects.get(pk=ty)
    chilFormset = inlineformset_factory(User, User1Profile, fields=('address','city','state','pin_code','country',), extra=1,)
    if request.method == 'POST':
        print("1")
        formset = chilFormset(request.POST, instance=pare)
        if formset.is_valid():
            formset.save()
            print("3")
            messages.success(request, 'Your account has been updated!')
            return redirect('index')
    print("2")
    category = Category.objects.all()
    formset = chilFormset(instance=pare)
    context = {
        'category': category,
        'formset': formset
    }
    return render(request, 'user_addressupdate.html', context)

login_required(login_url='/login')
def password_update(request):
    return HttpResponse('User Update')

@login_required(login_url='/login')
def user_contactupdate(request):
    current_user = request.user  # Access User Session information
    ty = current_user.id
    print(ty)
    pare=User.objects.get(pk=ty)
    chilFormset = inlineformset_factory(User, User2Profile, fields=('phone',), extra=1,)
    if request.method == 'POST':
        formset = chilFormset(request.POST, instance=pare)
        if formset.is_valid():
            formset.save()
            return redirect('index')
    category = Category.objects.all()
    formset = chilFormset(instance=pare)
    context = {
        'category': category,
        'formset': formset
    }
    return render(request, 'user_contactupdate.html', context)

@login_required(login_url='/login') # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        #category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password.html', {'form': form,#'category': category
                       })


