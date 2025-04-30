import hmac
import hashlib
import time
from ..client import DuitkuClient, DuitkuResult

class InvoiceService:
    def __init__(self, client: DuitkuClient):
        """
        Initializes the InvoiceService with a given DuitkuClient.

        :param client: An instance of DuitkuClient used to handle API requests.
        """
        self.client = client
        self.base_url = self.client.get_pop_base_url()

    def create(
        self, 
        request: dict,
    ) -> DuitkuResult:
        """
        Create a new invoice using the given request.
        
        The request should contain at least the following parameters:
        
        - paymentAmount
        - merchantOrderId
        - productDetails
        - email
        - callbackUrl
        - returnUrl
        
        The response will contain the following parameters:
        
        - merchantCode
        - reference
        - paymentUrl
        - amount
        - statusCode
        - statusMessage
        
        :param request: A dictionary containing the request parameters
        :return: A DuitkuResult object containing the response parameters
        """
        path = "/merchant/createInvoice"
        headers = {
            "x-duitku-merchantcode": self.client.merchant_code,
            "x-duitku-timestamp": str(int((round(time.time() * 1000)))),
        }
        headers["x-duitku-signature"] = self._generate_invoice_signature(headers["x-duitku-timestamp"])
        url = self.base_url + path

        result = self.client.send_api_request(
            method="POST",
            url=url,
            req_body=request,
            header_params=headers
        )
        return result
    
    def _generate_invoice_signature(self, timestamp: str) -> str:
        """
        Generates a signature for invoice creation using the given timestamp and the merchant's API key.

        :param timestamp: A string representing the current timestamp in milliseconds
        :return: A string representing the signature
        """
        str_signature = self.client.merchant_code + timestamp
        return hmac.new(
            self.client.api_key.encode(),
            str_signature.encode(),
            hashlib.sha256
        ).hexdigest()
