from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, TarjetasUsuario
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'
    required = True

class SimpleSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100, label='Nombres', required=True)
    last_name = forms.CharField(max_length=100, label='Apellidos', required=True)
    nacimiento = forms.DateField(widget=DateInput)
    dpi = forms.CharField(max_length=20, required=True)
    
    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.nacimiento = self.cleaned_data['nacimiento']
        user.dpi = self.cleaned_data['dpi']
        user.save()
        return user


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email','username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email','username',)


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'nacimiento',
            'password',
            'dpi',
            ]
        labels = {
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email',
            'nacimiento': 'Fecha De nacimiento',
            'password': 'password',
            'dpi': 'dpi',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'dpi': forms.TextInput(attrs={'class':'form-control'})
        }

class tarjetaForm(forms.ModelForm):
    class Meta:
        model = TarjetasUsuario
        fields = [
            'id_user',
            #'id_tarjeta',
            #'valor_tarjeta'
            ]
        labels = {
            'id_user': 'nombre',
            #'id_tarjeta': 'tarjeta',
            #'valor_tarjeta': 'valor',
        }
        widgets = {
            'id_user': forms.Select(attrs={'class':'form-control'}),
           # 'id_tarjeta': forms.TextInput(attrs={'class':'form-control'}),
            #'valor_tarjeta': forms.TextInput(attrs={'class':'form-control'})
        } 

