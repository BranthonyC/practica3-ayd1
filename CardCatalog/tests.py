from django.test import TestCase
from unittest.mock import MagicMock, patch
from .views import *
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
        mock_cp.data = [{"total": "7.77"}]
        print(ResponseJson[0].get("total"))
        self.assertEqual(mock_cp.data, ResponseJson)
        self.assertEqual(mock_cp.data[0].get("total"), ResponseJson[0].get("total"))

    def test_convertirPrecio(self):
        mock_cp = MagicMock(return_value=388.5)   
        mock_cp.convertirPrecio = 388.5
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

        
