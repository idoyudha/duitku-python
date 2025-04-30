import unittest
import os

import duitku

from http import HTTPStatus
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class TestInvoice(unittest.TestCase):
    duitku = duitku.Duitku()

    client = duitku.client
    client.merchant_code = os.getenv('MERCHANT_CODE')
    client.api_key = os.getenv('API_KEY')

    def test_create_invoice_success(self):
        create_invoice_req = {
            "paymentAmount": 10001,
            "merchantOrderId": datetime.now().strftime("%Y%m%d%H%M%S"),
            "productDetails": "test invoice",
            "email": "test@duitku.com",
            "callbackUrl": "https://duitku.com/callback",
            "returnUrl": "https://duitku.com"
        }

        result = self.duitku.invoice.create(create_invoice_req)
        self.assertEqual(result.status_code, HTTPStatus.OK)
        self.assertEqual(result.message['merchantCode'], self.client.merchant_code)
        self.assertIsInstance(result.message['reference'], str)
        self.assertIsNotNone(result.message['paymentUrl'])
        self.assertIsNotNone(result.message['amount'])
        self.assertEqual(result.message['statusCode'], '00')
        self.assertEqual(result.message['statusMessage'], 'SUCCESS')

    def test_create_invoice_bad_request(self):
        create_invoice_req = {}
        result = self.duitku.invoice.create(create_invoice_req)
        self.assertEqual(result.status_code, HTTPStatus.BAD_REQUEST)
        self.assertIsNotNone(result.message)

if __name__ == '__main__':
    unittest.main()