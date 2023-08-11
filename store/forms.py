from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=13)

    class Meta:
        model = User 
        fields = ['username', 'email','phone_number','last_name','first_name', 'password1', 'password2']