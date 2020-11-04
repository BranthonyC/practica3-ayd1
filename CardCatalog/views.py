from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

import requests
from django.views.generic import TemplateView, ListView
from .forms import *
from .models import *
from users.models import *

class detalle_transaccionListView(ListView):
    model = transaccion
    template_name = "giftcard/history.html"
    context_object_name = "lista_transacciones"

    def get_queryset(self):
        return transaccion.objects.filter(id_user=self.request.user)

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

def getPrecios():
    resC = requests.get('https://my-json-server.typicode.com/CoffeePaw/AyD1API/Card')
    dataC = json.loads(resC.text)
    resP = requests.get('https://my-json-server.typicode.com/CoffeePaw/AyD1API/Value')
    dataP = json.loads(resP.text)

    for tarjeta in dataC:
        for lPrice in tarjeta['availability']:
            for objPrice in resP:
                if str(lPrice) == str(objPrice['id']):
                    lPrice = objPrice['total']
    
    return dataC

def BuyGiftcard(request):
    cards = getCards()
    prices = getValues()
    temp = detalle_transaccion.objects.filter(id_trans=None)
    activa = 0
    
    if temp.count() > 0:
        activa = 1
    else:
        activa = 0

    return render(request,'giftcard/buy_giftcard.html',{'cards': cards, 'prices': prices, 'activa': activa})#, 'el_form': form})


def carrito(request):
    cards = getCards()
    prices = getValues()
    temp = detalle_transaccion.objects.filter(id_trans=None)
    nombre = "nada"
    cant_ = "1"
    activa = 1
    #temp = detalle_transaccion.objects.all()

    if len(temp) > 0:
        activa = 1
    else:
        activa = 0
    
    if request.method == 'POST':
        query = request.POST
        nombre = query.get('names', "nada")
        if nombre != "nada":

            if query['cant'] != '':
                cant_ = query['cant']

            precio_unit = float(query['precio'])+(float(query['precio'])*float(query['recargo']))
            nombre = query.get('names', "nada")
            
            compra=detalle_transaccion(
                id_card=query['id_card'],
                cant = cant_,
                precio = precio_unit,
                val_card=query['precio'],
            )
            compra.save()
    else:
        compra=detalle_transaccion(
            id_card=0,
            cant = 0,
            precio = 0.0,
        )
    
    return render(request,'giftcard/buy_giftcard.html',{'cards': cards, 'prices': prices, 'compra': temp, 'nombre': nombre, 'activa': activa})#, 'el_form': form})


def save_trans(request):
    query = request.POST
    temp = detalle_transaccion.objects.filter(id_trans=None)
    total = 0.0

    for temp2 in temp:
        print(temp2.cant)
        print(temp2.precio)
        total = total + (float(temp2.cant) * float(temp2.precio))
        print(total)
    
    trans = transaccion(
        id_user=request.user,
        total=total,
    )
    trans.save()

    for temp2 in temp:
        temp2.id_trans = trans
        temp2.save()

    return HttpResponseRedirect('/payment/'+str(trans.id))


def pago_Tarjeta(request, id):
    id_trans = id
    trans = transaccion.objects.get(pk=id)
    total_q = convertirPrecio(trans.total)
    monto = 0.0
    print(request)
    if request.method == 'POST':
        query = request.POST
        moneda = query['moneda']

        if moneda == "Quetzales":
            monto = str(total_q)
        else:
            monto = str(trans.total)

        pago_trans=tarjeta_transaccion(
            numero_tarjeta = query['numero_tarjeta'],
            nombre_tarjeta = query['nombre_tarjeta'],
            fecha_expiracion = query['fecha_expiracion'],
            codigo = query['codigo'],
            monto = monto,
            moneda = query['moneda'],
            estado = "Exitoso",
            id_trans = trans,
        )
        pago_trans.save()
        #Agrego la(s) tarjeta(s) a la tarjetas del usuario
        det_trans=detalle_transaccion.objects.filter(id_trans=trans)
        
        for detalle in det_trans:
            cantidad_tarjetas = (int(detalle.cant))
            cont = 0
            while cont < cantidad_tarjetas:

                userTarjet = TarjetasUsuario(
                    id_user = request.user,
                    id_tarjeta = detalle.id_card,
                    valor_tarjeta = detalle.val_card,
                )
                userTarjet.save()
                cont=cont+1
        #print(numero_tarjeta + nombre_tarjeta + fecha_expiracion + codigo + monto + moneda + total_q + estado)
        #form1 = pagoforms(request.POST)
        #if form1.is_valid():
        #    pago = form1.save(commit=False)
        #    pago.creador = trans
        #    #pago.save()
        #    messages.success(request, 'Bodega registrada correctamente')
        return HttpResponseRedirect('/carrito/')
    else:
        messages.error(request, 'No cumple con requisitos')
        form1=pagoforms()
    return render(request,'giftcard/payment.html',{'id_trans': id_trans, 'trans': trans, 'total_q': total_q})

# def save_trans(request):
#     print("========================")
#     prices = getValues()
#     for price in prices
#         print(price['total'])

#     return render(request,'giftcard/transac.html')


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
