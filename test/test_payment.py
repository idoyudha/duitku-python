import unittest
import requests
import os

import duitku

from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class TestPayment(unittest.TestCase):
    duitku = duitku.Duitku()

    client = duitku.client
    client.merchant_code = os.getenv('MERCHANT_CODE')
    client.api_key = os.getenv('API_KEY')

    def test_get_payment_methods_success(self):
        request_get_payment_methods = {
            "amount": 10001,
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        response = None
        try:
            response = self.duitku.payment.get_methods(request_get_payment_methods)
        except requests.exceptions.HTTPError as e:
            self.assertIsNone(e)
        self.assertIsInstance(response['paymentFee'], list)
        self.assertIsInstance(response['paymentFee'][0]['paymentMethod'], str)
        self.assertIsInstance(response['paymentFee'][0]['paymentName'], str)
        self.assertIsInstance(response['paymentFee'][0]['paymentImage'], str)
        self.assertIsInstance(response['paymentFee'][0]['totalFee'], str)
        self.assertEqual(response['responseCode'], '00')
        self.assertEqual(response['responseMessage'], 'SUCCESS')

if __name__ == '__main__':
    unittest.main()