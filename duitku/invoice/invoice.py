import hmac
import hashlib
from ..client import DuitkuClient
from .models import CreateInvoiceRequest, CreateInvoiceResponse

class InvoiceService:
    def __init__(self, client: DuitkuClient):
        self.client = client
        self.base_url = self.client.get_pop_base_url()

    def create(
        self, 
        request: CreateInvoiceRequest,
    ) -> CreateInvoiceResponse:
        path = "/merchant/createInvoice"
        headers = {
            "mechantCode": self.client.merchant_code,
            "timestamp": self.client.get_current_timestamp(),
        }
        headers["signature"] = self._generate_invoice_signature(headers["timestamp"])
        url = self.base_url + path

        response = self.client.send_api_request(
            method="POST",
            url=url,
            req_body=request,
            header_params=headers
        )
        return response.json()
    
    def _generate_invoice_signature(self, timestamp: str) -> str:
        str_signature = self.client.merchant_code + timestamp
        return hmac.new(
            self.client.api_key.encode(),
            str_signature.encode(),
            hashlib.sha256
        ).hexdigest()
