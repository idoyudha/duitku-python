import json
import time
import requests
from typing import Optional, Dict, Any

class DuitkuClient():
    SandboxV2BaseURL = 'https://sandbox.duitku.com/webapi/api'
    ProductionV2BaseURL = 'https://passport.duitku.com/webapi/api'
    SandboxPOPBaseURL = 'https://api-sandbox.duitku.com/api'
    ProductionPOPBaseURL = 'https://api-prod.duitku.com/api'
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
    ) -> requests.Response:
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
        # print(data)
        # print(response.text)
        response.raise_for_status()
        return response
        