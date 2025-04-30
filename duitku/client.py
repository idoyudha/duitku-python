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
        self.merchant_code = merchant_code
        self.api_key = api_key
        self.environment = environment

    def get_v2_base_url(self):
        if self.environment == "sandbox":
            return self.SandboxV2BaseURL
        else:
            return self.ProductionV2BaseURL
        
    def get_pop_base_url(self):
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
        