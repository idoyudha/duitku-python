import unittest
import duitku

from datetime import datetime

class TestInvoice(unittest.TestCase):
    duitku = duitku.Duitku()

    client = duitku.client
    client.merchant_code = 'YOUR MERCHANT CODE'
    client.api_key = 'YOUR API KEY'

    def test_create_invoice_success(self):
        create_invoice_req = {
            "paymentAmount": 10001,
            "merchantOrderId": datetime.now().strftime("%Y%m%d%H%M%S"),
            "productDetails": "test invoice",
            "email": "test@duitku.com",
            "callbackUrl": "https://duitku.com/callback",
            "returnUrl": "https://duitku.com"
        }

        response = self.duitku.invoice.create(create_invoice_req)
        self.assertEqual(response['merchantCode'], self.client.merchant_code)
        self.assertIsInstance(response['reference'], str)
        self.assertIsNotNone(response['paymentUrl'])
        self.assertIsNotNone(response['amount'])
        self.assertEqual(response['statusCode'], '00')
        self.assertEqual(response['statusMessage'], 'SUCCESS')

if __name__ == '__main__':
    unittest.main()