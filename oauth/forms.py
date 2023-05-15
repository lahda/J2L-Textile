from django import forms
from django.contrib.auth.forms import UserCreationForm

from oauth.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=150, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email@example.com'}))
    password = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email@example.com'}))
    password1 = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
    password2 = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')