import hashlib

from ..client import DuitkuClient

class PaymentService:
    def __init__(self, client: DuitkuClient):
        self.client = client
        self.base_url = self.client.get_v2_base_url()

    def get_methods(
        self,
        request: dict,
    ) -> dict:
        path = "/merchant/paymentmethod/getpaymentmethod"
        request['merchantCode'] = self.client.merchant_code
        request['signature'] = self._generate_payment_signature(str(request['amount']) + request['datetime'])
        url = self.base_url + path
        response = self.client.send_api_request(
            method="POST",
            url=url,
            req_body=request,
        )
        return response

    def _generate_payment_signature(self, paramter: str) -> str:
        combined_str = self.client.merchant_code + paramter + self.client.api_key
        hash_bytes = hashlib.sha256(combined_str.encode()).digest()
        return hash_bytes.hex()