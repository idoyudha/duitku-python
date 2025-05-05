# Transaction Service

## Create Transaction

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

request_create_transaction = {
    "paymentAmount": 10000,
    "merchantOrderId": datetime.now().strftime("%Y%m%d%H%M%S"),
    "productDetails": "test create transaction example",
    "email": "sales@example.com",
    "paymentMethod": "VC",
    "customerVaName": "Test Transaction",
    "callbackUrl": "https://example.com/callback",
    "returnUrl": "https://example.com"
}

result = duitku.transaction.create(request_create_transaction)

# Process response body
print(result.message)
```

## Get Status
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

request_get_transaction = {
    "merchantOrderId": "YOUR_MERCHANT_ORDER_ID"
}

result = duitku.transaction.get_status(request_get_transaction)

# Process response body
print(result.message)
```