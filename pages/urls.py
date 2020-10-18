from django.urls import path
from .views import HomePageView
from users.views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('SignUp/', signUp, name='SignUp'),
    #path('Modificar_Perfil/<id>', modificar_perfil, name='modificar_perfil'),
    path('Perfil/', mostrar_perfil, name='mostrar_perfil'),
]