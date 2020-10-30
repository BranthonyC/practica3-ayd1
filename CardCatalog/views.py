from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from django.views.generic import TemplateView
from .forms import cardForm
from .models import detalle_transaccion

# Create your views here.
def getAPI_TasaCambio():
    response = requests.get('https://my-json-server.typicode.com/CoffeePaw/AyD1API/TasaCambio')
    return response.json()

def convertirPrecio(valor):
    tipoCambio=getAPI_TasaCambio()[0].get("total")
    valorConvertido=float(tipoCambio)*valor
    return valorConvertido

def getCards():
    response = requests.get('https://my-json-server.typicode.com/CoffeePaw/AyD1API/Card')
    return response.json()
# Precio
def getValues():
    response = requests.get('https://my-json-server.typicode.com/CoffeePaw/AyD1API/Value')
    return response.json()

def BuyGiftcard(request):
    cards = getCards()
    prices = getValues()
    #form = cardForm(request.POST or None)
  
    return render(request,'giftcard/buy_giftcard.html',{'cards': cards, 'prices': prices})#, 'el_form': form})

def save_trans(request):
    print("========================")
    prices = getValues()
    for price in prices
        print(price['total'])

    return render(request,'giftcard/transac.html')


# id_card = models.CharField(max_length=5)
# cant = models.CharField(max_length=5)
# precio = models.CharField(max_length=5)
# id_trans = models.ForeignKey(transaccion, on_delete

# def agregarDetalle(request, id_card, cant, precio):

#     if request.method == 'POST':
#         form1 = bodega_forms(request.POST)
#         if form1.is_valid():
#             print("Empezando")
#             bodega = form1.save(commit=False)
#             bodega.creador = prueba
#             bodega.save()
#             print("Exito")

#             return HttpResponseRedirect('/lista_bodegas/'+id)

#     else:
#         form1=bodega_forms()
#     return render(request,'bodegas/registro_bodega.html',{'form1': form1})