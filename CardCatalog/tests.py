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