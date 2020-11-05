from django.test import TestCase
from unittest.mock import MagicMock, patch
from django.urls import reverse, resolve
from .views import *
from .models import *
from django.contrib.auth import get_user_model
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
        mock_cp.data = [{"total": "7.85"}]
        print(ResponseJson[0].get("total"))
        self.assertEqual(mock_cp.data, ResponseJson)
        self.assertEqual(mock_cp.data[0].get("total"), ResponseJson[0].get("total"))

    def test_convertirPrecio(self):
        mock_cp = MagicMock(return_value=392.5)   
        mock_cp.convertirPrecio = 392.5
        self.assertEqual(mock_cp(), convertirPrecio(50))



class Tests_Mod(TestCase):
    def test_request_response_cards(self):
        # Send a request to the API server and store the response.
        response = requests.get('https://my-json-server.typicode.com/CoffeePaw/AyD1API/Card')
        cards = response.json()
        #print(cards)
        mock_card = MagicMock()
        mock_card.data = [{
                                "id": "6",
                                "name": "Google Play",
                                "image": "https://media.karousell.com/media/photos/products/2020/5/21/rm50_goggle_play_gift_card_mal_1590040469_c1100b5a_progressive.jpg",
                                "chargeRate": 1,
                                "active": "false",
                                "availability": "[1,2,4]"
                            },
                            {
                                "id": "2",
                                "name": "PlayStation",
                                "image": "https://www.allkeyshop.com/blog/wp-content/uploads/PlayStationNetworkGiftCard.jpg",
                                "chargeRate": 0.25,
                                "active": "false",
                                "availability": "[1,3]"
                            }]
        # Confirm that the request-response cycle completed successfully.
        print(mock_card.data[1].get("name"))
        print(cards[1].get("name"))
        self.assertTrue(response.ok)
        self.assertEqual(mock_card.data[1].get("name"), cards[1].get("name"))

    def test_request_response_values(self):
        # Send a request to the API server and store the response.
        response = requests.get('https://my-json-server.typicode.com/CoffeePaw/AyD1API/Value')
        values = response.json()
        #print(values)
        mock_val = MagicMock()
        mock_val.data = [{"id": "1","total": "10"},{"id": "2","total": "25"},{"id": "3","total": "50"},{"id": "4","total": "100"}]
        # Confirm that the request-response cycle completed successfully.
        print(mock_val.data[3].get("total"))
        print(values[3].get("total"))
        self.assertTrue(response.ok)
        self.assertEqual(mock_val.data,values)
        self.assertEqual(mock_val.data[3].get("total"), values[3].get("total"))


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
        
class Alfanumerico_Test(TestCase):
    def test_alfanumerico(self):
        alfanumerico = id_generator()
        self.assertEqual(len(alfanumerico),8)
        