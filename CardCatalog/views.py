from django.shortcuts import render
import requests

# Create your views here.
def getAPI_TasaCambio():
    response = requests.get('https://my-json-server.typicode.com/CoffeePaw/AyD1API/TasaCambio')
    return response.json()

def convertirPrecio(valor):
    tipoCambio=getAPI_TasaCambio()[0].get("total")
    valorConvertido=float(tipoCambio)*valor
    return valorConvertido