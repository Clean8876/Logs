from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

#create a costumn form to make change sin orginal form
class Userregister(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length= 250,label='username')
    password = forms.CharField(label='password',widget= forms.PasswordInput)

    error_messages = {
        'invalid_login': "Please enter a correct %(username)s and password. Note that both fields may be case-sensitive.",
        'inactive': "This account is inactive.",
    }








