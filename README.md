# Duitku Python API Client Library
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

Duitku API Library for Python
## Supported Feature
|        Feature         |              Function                |                HTTP Request                   |              Description              |
|------------------------|--------------------------------------|-----------------------------------------------|---------------------------------------|
| Get Payment Method     | client.payment.get_methods           | POST /merchant/paymentmethod/getpaymentmethod | Get list of available payment methods |
| Craete New Invoice     | client.invoice.create                | POST /merchant/createInvoice                  | Create Transaction via POP API        |

## Requirements
- Python 3.5 or later
- Duitku account, [register here](https://dashboard.duitku.com/Account/Register)
- [API Key](https://docs.duitku.com/en/account/#account-integration--getting-api-key)

## Documentation
- https://docs.duitku.com/

## Installation
Get this library, add to your project

```bash
pip install duitku
```

## Example Usage
```python
import requests
import duitku

from http import HTTPStatus
from datetime import datetime

duitku = duitku.Duitku()

client = duitku.client
client.merchant_code = "YOUR MERCHANT CODE"
client.api_key = "YOUR API KEY"
client.environment = client.SandboxEnv

create_invoice_req = {
    "paymentAmount": 10001,
    "merchantOrderId": datetime.now().strfti("%Y%m%d%H%M%S"),
    "productDetails": "test invoice",
    "email": "test@duitku.com",
    "callbackUrl": "https://duitku.com/callback",
    "returnUrl": "https://duitku.com"
}
response = None
try:
    response = duitku.invoice.create(create_invoice_req):
except requests.exceptions.HTTPError as e:
    print(e)
print(response)
```

## Support
If you have a feature request or spotted a bug or a techical problem, [create an issue here](https://github.com/idoyudha/duitku-python/issues/new/choose).
For other questions, please contact duitku through their live chat on your dashboard.

## License
MIT license. For more information, see the LICENSE file.