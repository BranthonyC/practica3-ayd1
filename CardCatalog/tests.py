from django.test import TestCase
from unittest.mock import MagicMock, patch
from .views import *
import requests


class CardTests(TestCase):

    def setUp(self):
        self.tarjeta = tarjeta_transaccion.objects.create(numero_tarjeta='1234567891234567')

    def card_correct_mask(self):
        self.assertEqual(self.tarjeta,'1234XXXXXXXX4567')


class Response_Tests(TestCase):
    def test_request_response_TasaCambio(self):
        # Send a request to the API server and store the response.
        response = requests.get('https://my-json-server.typicode.com/CoffeePaw/AyD1API/TasaCambio')
        print(response.json())
        # Confirm that the request-response cycle completed successfully.
        self.assertTrue(response.ok)

    def test_view_getAPI_TasaCambio(self):
        ResponseJson=getAPI_TasaCambio()
        mock_cp = MagicMock()   
        mock_cp.data = [{"total": "7.77"}]
        print(ResponseJson[0].get("total"))
        self.assertEqual(mock_cp.data, ResponseJson)
        self.assertEqual(mock_cp.data[0].get("total"), ResponseJson[0].get("total"))

    def test_convertirPrecio(self):
        mock_cp = MagicMock(return_value=388.5)   
        mock_cp.convertirPrecio = 388.5
        self.assertEqual(mock_cp(), convertirPrecio(50))

class servicio(TestCase):

    def test_request_response_cards(self):
        # Send a request to the API server and store the response.
        response = requests.get('https://my-json-server.typicode.com/CoffeePaw/AyD1API/Card')
        info = response.json()
        print(info)
        # Confirm that the request-response cycle completed successfully.
        self.assertTrue(response.ok)

    def test_request_response_cards(self):
        # Send a request to the API server and store the response.
        response = requests.get('https://my-json-server.typicode.com/CoffeePaw/AyD1API/Value')
        info = response.json()
        print(info)
        #print(info[0].get("name"))
        # Confirm that the request-response cycle completed successfully.
        self.assertTrue(response.ok)

    