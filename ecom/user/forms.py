from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput

from user.models import User1Profile
from user.models import User2Profile


class SignUp1Form(UserCreationForm):
    username = forms.CharField(max_length=30, label='User Name :',
                               widget=forms.TextInput
                               (attrs={'class': 'form-control', 'style': 'width:500px', 'size': '10',
                                       'required': ''}))
    email = forms.EmailField(max_length=200, label='Email :',
                             widget=forms.EmailInput
                             (attrs={'class': 'form-control', 'style': 'width:500px', 'required': ''}))
    first_name = forms.CharField(max_length=100, help_text='First Name', label='First Name :',
                                 widget=forms.TextInput
                                 (attrs={'class': 'form-control', 'style': 'width:500px', 'required': ''}))
    last_name = forms.CharField(max_length=100, help_text='Last Name', label='Last Name :',
                                widget=forms.TextInput
                                (attrs={'class': 'form-control', 'style': 'width:500px', 'required': ''}))
    password1 = forms.CharField(max_length=100, help_text='Password', label='Password :',
                                widget=forms.PasswordInput
                                (attrs={'class': 'form-control', 'style': 'width:500px', 'required': ''}))
    password2 = forms.CharField(max_length=100, help_text='Password', label='Password Confirmation :',
                                widget=forms.PasswordInput
                                (attrs={'class': 'form-control', 'style': 'width:500px', 'required': ''}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)


class SignUp2Form(forms.ModelForm):
    address = forms.CharField(max_length=100, label='Address :',
                              widget=forms.TextInput
                              (attrs={'class': 'form-control', 'style': 'width:500px', 'required': ''}))
    city = forms.CharField(max_length=100, label='City :',
                           widget=forms.TextInput
                           (attrs={'class': 'form-control', 'style': 'width:500px', 'required': ''}))
    state = forms.CharField(max_length=100, label='State :',
                            widget=forms.TextInput
                            (attrs={'class': 'form-control', 'style': 'width:500px', 'required': ''}))
    pin_code = forms.IntegerField(label='Pin Code :',
                                  widget=forms.TextInput
                                  (attrs={'type':'number', 'class': 'form-control', 'style': 'width:500px', 'required': ''}))
    country = forms.CharField(max_length=100, label='Country :',
                              widget=forms.TextInput
                              (attrs={'class': 'form-control', 'style': 'width:500px', 'required': ''}))

    class Meta:
        model = User1Profile
        fields = ('address', 'city', 'state', 'pin_code', 'country')


class SignUp3Form(forms.ModelForm):
    phone = forms.IntegerField(label='Phone :',
                               widget=forms.TextInput
                               (attrs={'type':'number', 'class': 'form-control', 'style': 'width:500px', 'required': ''}))

    class Meta:
        model = User2Profile
        fields = ('phone',)


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username', 'required': ''}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email', 'required': ''}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name', 'required': ''}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name', 'required': ''}),
        }
