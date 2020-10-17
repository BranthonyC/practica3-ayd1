from django.urls import path
from .views import HomePageView
from users.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('SignUp/', signUp, name='SignUp'),
]