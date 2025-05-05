# Invoice Service

## Create Invoice

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

# Create request body for invoice
create_invoice_req = {
    "paymentAmount": 20000,
    "merchantOrderId": datetime.now().strfti("%Y%m%d%H%M%S"),
    "productDetails": "the best example product",
    "email": "sales@example.com",
    "callbackUrl": "https://example.com/callback",
    "returnUrl": "https://example.com"
}

result = duitku.invoice.create(create_invoice_req)

# Process response body
print(response.message)
```