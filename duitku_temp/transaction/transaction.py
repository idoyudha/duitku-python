import hashlib

from ..client import DuitkuClient, DuitkuResult

class TransactionService:
    def __init__(self, client: DuitkuClient):
        self.client = client
        self.base_url = self.client.get_v2_base_url()

    def create(
        self,
        request: dict
    ) -> DuitkuResult:
        """
        Create a new transaction.

        :param request: A dictionary containing the request parameters.
        :return: A DuitkuResult object containing the response parameters.
        """
        path = "/merchant/v2/inquiry"
        request['merchantCode'] = self.client.merchant_code
        request['signature'] = self._generate_transaction_signature(request.get('merchantOrderId', '') +  str(request.get('paymentAmount')))
        url = self.base_url + path

        result = self.client.send_api_request(
            method="POST",
            url=url,
            req_body=request,
            header_params=None
        )
        return result
    
    def get_status(
        self,
        request: dict
    ) -> DuitkuResult:
        """
        Get the status of a transaction.

        :param request: A dictionary containing the request parameters.
        :return: A DuitkuResult object containing the response parameters.
        """
        path = "/merchant/transactionStatus"
        request['merchantCode'] = self.client.merchant_code
        request['signature'] = self._generate_transaction_signature(request['merchantOrderId'])
        url = self.base_url + path

        result = self.client.send_api_request(
            method="POST",
            url=url,
            req_body=request,
            header_params=None
        )
        return result
    
    def _generate_transaction_signature(self, parameter: str) -> str:
        """
        Generates a transaction signature using the given parameter, merchant code, and API key.

        :param parameter: A string containing the request parameters.
        :return: A string representing the generated signature in hexadecimal format.
        """
        combined_str = self.client.merchant_code + parameter + self.client.api_key
        return hashlib.md5(combined_str.encode()).digest().hex()