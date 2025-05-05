# Payment Service

## Get Payment Method

```python
import Duitku

from datetime import datetime

# Initialize duitku class
duitku = Duitku.Duitku()

# Initialize duitku client
client = duitku.client
client.merchant_code ='YOUR_MERCHANT_CODE'
client.api_key = 'YOUR_API_KEY'

# NOTE: no need to initialize duitku class and client if you already had initialized

# Create request body for get payment method
request_get_payment_methods = {
    "amount": 10001,
    "datetime": datetime.now().strftime("%Y-%m-%%H:%M:%S"),
}

result = duitku.payment.get_methods(request_get_payment_methods)

# Process response body
print(response.message)
```