import unittest
import os

import duitku

from http import HTTPStatus
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

        result = self.duitku.payment.get_methods(request_get_payment_methods)
        self.assertEqual(result.status_code, HTTPStatus.OK)

        self.assertIsInstance(result.message['paymentFee'], list)
        self.assertIsInstance(result.message['paymentFee'][0]['paymentMethod'], str)
        self.assertIsInstance(result.message['paymentFee'][0]['paymentName'], str)
        self.assertIsInstance(result.message['paymentFee'][0]['paymentImage'], str)
        self.assertIsInstance(result.message['paymentFee'][0]['totalFee'], str)
        self.assertEqual(result.message['responseCode'], '00')
        self.assertEqual(result.message['responseMessage'], 'SUCCESS')

if __name__ == '__main__':
    unittest.main()