import hmac
import hashlib
import time
from ..client import DuitkuClient, DuitkuResult

class InvoiceService:
    def __init__(self, client: DuitkuClient):
        self.client = client
        self.base_url = self.client.get_pop_base_url()

    def create(
        self, 
        request: dict,
    ) -> DuitkuResult:
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
        str_signature = self.client.merchant_code + timestamp
        return hmac.new(
            self.client.api_key.encode(),
            str_signature.encode(),
            hashlib.sha256
        ).hexdigest()
