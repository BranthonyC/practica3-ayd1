from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import CustomUser
from .forms import UserForm
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login



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
