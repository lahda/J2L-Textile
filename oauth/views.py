from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from oauth.forms import LoginForm, RegisterForm
from oauth.models import User

from index.views import index

# Create your views here.
def login_user(request):
    login_form = LoginForm()
    
    context = {
        'form': login_form
    }
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'connexion reussie')
            return redirect(index)
        else:
            messages.error(request, 'informations de connexion incorrectes')
            return render(request, 'oauth/login.html', context)
    else:            
        return render(request, 'oauth/login.html', context)


def register(request):
    register_form = RegisterForm()
    
    context = {
        'form': register_form
    }
    
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                print("exists")
                messages.error(request, 'Cet email est déjà utilisé par un autre utilisateur')
            else:
                register_form.save()
                print("save")
                return redirect(login_user)
        else:
            print("invalid")
            messages.error(request, 'informations de connexion incorrectes')
            return render(request, 'oauth/register.html', context)
    else:            
        return render(request, 'oauth/register.html', context)