import unittest
import os

import duitku

from http import HTTPStatus
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class TestTransaction(unittest.TestCase):
    duitku = duitku.Duitku()

    client = duitku.client
    client.merchant_code = os.getenv('MERCHANT_CODE')
    client.api_key = os.getenv('API_KEY')

    test_merchant_order_id = datetime.now().strftime("%Y%m%d%H%M%S")

    def test_create_transaction_success(self):
        request_create_transaction = {
            "paymentAmount": 10001,
            "merchantOrderId": self.test_merchant_order_id,
            "productDetails": "test create transaction",
            "email": "test@duitku.com",
            "paymentMethod": "VC",
            "customerVaName": "Test Transaction",
            "callbackUrl": "https://duitku.com/callback",
            "returnUrl": "https://duitku.com"
        }

        result = self.duitku.transaction.create(request_create_transaction)
        self.assertEqual(result.status_code, HTTPStatus.OK)
        self.assertEqual(result.message['merchantCode'], self.client.merchant_code)
        self.assertIsInstance(result.message['reference'], str)
        self.assertIsNotNone(result.message['paymentUrl'])
        self.assertEqual(result.message['statusCode'], '00')
        self.assertEqual(result.message['statusMessage'], 'SUCCESS')

    def test_craete_transaction_unauthorized(self):
        request_create_transaction = {}
        result = self.duitku.transaction.create(request_create_transaction)
        self.assertEqual(result.status_code, HTTPStatus.UNAUTHORIZED)
        self.assertIsNotNone(result.message)

    def test_get_transaction_status(self):
        request_get_trx_status = {
            "merchantOrderId": self.test_merchant_order_id
        }
        result = self.duitku.transaction.get_status(request_get_trx_status)
        self.assertEqual(result.status_code, HTTPStatus.OK)
        self.assertEqual(result.message['merchantOrderId'], self.test_merchant_order_id)
        self.assertIsNotNone(result.message['reference'])
        self.assertIsNotNone(result.message['amount'])
        self.assertIsNotNone(result.message['statusCode'])
        self.assertIsNotNone(result.message['statusMessage'])

if __name__ == '__main__':
    unittest.main()