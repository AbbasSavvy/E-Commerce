from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from user.models import User1Profile
from user.models import User2Profile
from django.forms import inlineformset_factory


class SignUp1Form(UserCreationForm):
    username = forms.CharField(max_length=30,label= 'User Name :')
    email = forms.EmailField(max_length=200,label= 'Email :')
    first_name = forms.CharField(max_length=100, help_text='First Name',label= 'First Name :')
    last_name = forms.CharField(max_length=100, help_text='Last Name',label= 'Last Name :')


    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )

class SignUp2Form(forms.ModelForm):
    address = forms.CharField(max_length=100,label= 'Address :')
    city = forms.CharField(max_length=100,label= 'City :')
    state = forms.CharField(max_length=100,label= 'State :')
    pin_code = forms.CharField(max_length=100,label= 'Pin Code :')
    country = forms.CharField(max_length=100,label= 'Country :')

    class Meta:
        model = User1Profile
        fields = ('address', 'city','state','pin_code','country')

class SignUp3Form(forms.ModelForm):
    phone = forms.CharField(max_length=100,label= 'Phone :')

    class Meta:
        model = User2Profile
        fields = ('phone',)


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username','email','first_name','last_name')
        widgets = {
            'username'  : TextInput(attrs={'class': 'input','placeholder':'username'}),
            'email'     : EmailInput(attrs={'class': 'input','placeholder':'email'}),
            'first_name': TextInput(attrs={'class': 'input','placeholder':'first_name'}),
            'last_name' : TextInput(attrs={'class': 'input','placeholder':'last_name' }),
        }
