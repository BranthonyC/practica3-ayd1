from django import forms
from django.forms import ModelForm
from .models import *

#from anotacion.models import models

class cardForm(forms.Form):
    id_card = forms.IntegerField()
    cant = forms.IntegerField()
    precio = forms.FloatField()
    id_trans = forms.IntegerField()

class pagoforms(forms.ModelForm):
    class Meta:
        model = tarjeta_transaccion
        fields = [
            'numero_tarjeta',
            'nombre_tarjeta',
            'fecha_expiracion',
            'codigo'
        ]


        # widgets = {
        #     'nombre': forms.TextInput(attrs={'class':'form-control'}),
        #     'apellido': forms.TextInput(attrs={'class':'form-control'}),
        #     'telefono': forms.TextInput(attrs={'class':'form-control'}),
        #     'telefono_emergencia': forms.TextInput(attrs={'class':'form-control'}),
        #     'correo': forms.TextInput(attrs={'class':'form-control'}),
        #     'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        #     'direccion': forms.TextInput(attrs={'class':'form-control'}),
        #     'descripccion': forms.TextInput(attrs={'class':'form-control'}),
        #     'sexo': forms.Select(attrs={'class':'form-control'})
        # }
