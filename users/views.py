from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import CustomUser
from .forms import UserForm
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template


# Create your views here.
def signUp(request):
    print("Holaa")
    form = UserForm(request.POST)
    #if request.method == 'POST':
    if form.is_valid():
        print("Si entro")
        form.save()
        #return redirect('pages:listado_pacientes')
        users=CustomUser.objects.all()
        data={
            'users_list':users
        }
        print("SIIIIIIIIUUUUUUUUUUUUU")
        return redirect('home')

    else:
        print("NOOOOOOOOOOOOOOOO")
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})
