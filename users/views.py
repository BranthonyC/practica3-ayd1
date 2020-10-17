from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import CustomUser
from .forms import UserForm
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import get_user_model
from django.contrib import messages


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

        username = form.cleaned_data['username']
        result = check_username(username)

        print("VERIFICANDOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        print(result)

        #Para que loguear luedo de su creación.
        do_login(request, user)
        return redirect('home')

    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})

def check_username(username):
    users=CustomUser.objects.get(username=username)
    return users