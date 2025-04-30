import hashlib

from ..client import DuitkuClient, DuitkuResult

class PaymentService:
    def __init__(self, client: DuitkuClient):
        """
        Initializes the PaymentService with a given DuitkuClient.

        :param client: An instance of DuitkuClient used to handle API requests.
        """
        self.client = client
        self.base_url = self.client.get_v2_base_url()

    def get_methods(
        self,
        request: dict,
    ) -> DuitkuResult:
        """
        Get a list of payment methods.

        :param request: A dictionary containing the request parameters
        :return: A DuitkuResult object containing the response parameters
        """
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
        """
        Generates a signature for the payment method request using the given parameter and the merchant's API key.

        :param paramter: A string containing the request parameters
        :return: A string representing the signature
        """
        combined_str = self.client.merchant_code + paramter + self.client.api_key
        return hashlib.sha256(combined_str.encode()).digest().hex()