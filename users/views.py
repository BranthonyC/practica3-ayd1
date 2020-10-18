from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import CustomUser
from .forms import UserForm
from django.http import HttpResponse
from django.views.generic import View, ListView
from django.template.loader import get_template
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import get_user_model
from django.contrib import messages

class UsersListView(ListView):
    model = CustomUser
    template_name = 'home.html'

# Create your views here.
def signUp(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save()

        #variables para usarlas posteriormente en el login.
        '''
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)'''
    
        #Para que loguear luedo de su creación.
        do_login(request, user)
        return redirect('home')

    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})

def check_username(username):
    users=CustomUser.objects.get(username=username)
    return users

def check_duplicate_username(username):
    if CustomUser.objects.filter(username=username).exists():
        return True
    return False

def check_duplicate_email(email):
    if CustomUser.objects.filter(email=email).exists():
        return True
    return False

def mostrar_perfil(request):
    usuario =CustomUser.objects.get(dpi=request.user.dpi) 
    if request.method == 'GET':
        form = UserForm(instance=usuario)
    
    return render(request,'account/perfil.html', {'form': form})


    