from django.shortcuts import render
import requests

# Create your views here.
def getAPI_TasaCambio():
    response = requests.get('https://my-json-server.typicode.com/CoffeePaw/AyD1API/TasaCambio')
    return response.json()