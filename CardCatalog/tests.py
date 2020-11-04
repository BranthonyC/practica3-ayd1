from django.test import TestCase
from unittest.mock import MagicMock, patch
from django.urls import reverse, resolve
from .views import *
from .models import *
from django.contrib.auth import get_user_model
import requests

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
        mock_cp.data = [{"total": "7.85"}]
        print(ResponseJson[0].get("total"))
        self.assertEqual(mock_cp.data, ResponseJson)
        self.assertEqual(mock_cp.data[0].get("total"), ResponseJson[0].get("total"))

    def test_convertirPrecio(self):
        mock_cp = MagicMock(return_value=392.5)   
        mock_cp.convertirPrecio = 392.5
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


class TestCompra(TestCase):
    def setUp(self):
        detalle_transaccion.objects.create(
            id_card= '1', cant= '12', precio= 35.35, val_card='5.5', id_trans=None)
        
        detalle_transaccion(
            id_card= '1', cant= '12', precio= 35.35, val_card='5.5', id_trans=None
        ).save()

        User = get_user_model()
        user = User.objects.create_user(
            username='Henry',
            email='henriscoh1995@gmail.com',
            password='testingpasscode123',
        )

        #check_user = get_user_model().objects.all()[0]
        #print(check_user)

        trans = transaccion(
            id_user=user,
            total=650.60,
        )
        trans.save()

    data={
        'id_card':'1',
        'cant':'12',
        'precio':35.35,
        'val_card':'5.5'
    }

    check_user = get_user_model().objects.all()
    check_trans = transaccion.objects.all()
        
    def test_Compra(self):
        response = self.client.post('/carrito/',self.data)
        self.assertEqual(response.status_code, 200)

    def test_pagoTarjeta(self):
        pago_trans=tarjeta_transaccion(
            numero_tarjeta = "1234567890123456",
            nombre_tarjeta = "Prueba",
            fecha_expiracion = "12/20",
            codigo = "ab1",
            monto = 650.60,
            moneda = "Quetzales",
            estado = "Exitoso",
            id_trans = self.check_trans[0],
        ).save()

        check_pago = tarjeta_transaccion.objects.all()

        self.assertEqual(self.check_user[0].username, 'Henry')
        self.assertEqual(self.check_trans[0].total, 650.60)
        self.assertEqual(check_pago[0].codigo, "ab1")