from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from user.forms import SignUp1Form, SignUp2Form, SignUp3Form

# Create your views here.
from django.utils import translation
from product.models import Category
from user.models import User1Profile, User2Profile


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

