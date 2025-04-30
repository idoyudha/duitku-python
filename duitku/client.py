import json
import requests

from http import HTTPStatus
from typing import Optional, Dict, Any


class DuitkuResult:
    def __init__(
        self,
        status_code=HTTPStatus.OK,
        message=None,
        raw_request="",
        raw_response=""
    ):
        """
        Initializes a DuitkuResult object.

        :param status_code: The HTTP status code of the response.
        :param message: The JSON response message.
        :param raw_request: The raw request body.
        :param raw_response: The raw response body.
        """
        self.status_code = status_code
        self.message = message
        self.raw_request = raw_request
        self.raw_response = raw_response

class DuitkuClient:
    SandboxV2BaseURL = 'https://sandbox.duitku.com/webapi/api'
    ProductionV2BaseURL = 'https://passport.duitku.com/webapi/api'
    SandboxPOPBaseURL = 'https://api-sandbox.duitku.com/api'
    ProductionPOPBaseURL = 'https://api-prod.duitku.com/api'
    SandboxEnv = 'sandbox'
    ProductionEnv = "production"
    def __init__(
        self, 
        merchant_code=None,
        api_key=None,
        environment="sandbox"
    ):
        """
        Initializes a DuitkuClient object.

        :param merchant_code: The merchant code obtained from Duitku.
        :param api_key: The API key obtained from Duitku.
        :param environment: The environment to use. Can be either "sandbox" or "production". Default is "sandbox".
        """
        self.merchant_code = merchant_code
        self.api_key = api_key
        self.environment = environment

    def get_v2_base_url(self):
        """
        Gets the base URL for the Duitku V2 API.

        :return: The base URL for the Duitku V2 API.
        """
        if self.environment == "sandbox":
            return self.SandboxV2BaseURL
        else:
            return self.ProductionV2BaseURL
        
    def get_pop_base_url(self):
        """
        Gets the base URL for the Duitku POP API.

        :return: The base URL for the Duitku POP API.
        """
        if self.environment == "sandbox":
            return self.SandboxPOPBaseURL
        else:
            return self.ProductionPOPBaseURL
        
    def send_api_request(
        self,
        method: str,
        url: str,
        req_body: Optional[Dict[str, Any]],
        header_params: Dict[str, str] = None
    ) -> DuitkuResult:
        """
        Sends a request to the Duitku API.

        :param method: The HTTP method to use.
        :param url: The URL to send the request to.
        :param req_body: The request body to send.
        :param header_params: Additional headers to include.
        :return: A DuitkuResult object containing the response.
        """
        headers = {"Content-Type": "application/json"}
        if header_params is not None:
            headers.update(header_params)

        if req_body is not None:
            data = json.dumps(req_body)
        else:
            data = None

        response = requests.request(
            method,
            url,
            headers=headers,
            data=data,
        )
        return self._handle_response(response)
    
    def _handle_response(self, response: requests.Response) -> DuitkuResult:
        """
        Handles the HTTP response from the Duitku API and returns a DuitkuResult object.

        :param response: The HTTP response object received from the API request.
        :return: A DuitkuResult object containing the status code, raw request, raw response,
                and parsed JSON message if available; otherwise, the raw text message.
        """
        result = DuitkuResult(
            status_code=response.status_code,
            raw_request=response.request.__dict__,
            raw_response=response.raw._original_response.__dict__,
        )
        try:
            if response.text:
                result.message = response.json()
        except json.decoder.JSONDecodeError:
            result.message = response.text
        return result
        