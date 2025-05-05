from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

import Duitku
import os


load_dotenv()

app = FastAPI()

# To run app in development mode, use command `fastapi dev main.py``

@app.get("/")
def read_root():
    return {"Hello": "Duitku Python SDK"}

duitku = Duitku.Duitku()

client = duitku.client
client.merchant_code = os.getenv('MERCHANT_CODE')
client.api_key = os.getenv('API_KEY')
client.environment = client.SandboxEnv

class CreateInvoiceReq(BaseModel):
    paymentAmount: int
    merchantOrderId: str
    productDetails: str
    email: str
    callbackUrl: str
    returnUrl: str

@app.post("/invoice")
def create_invoice(body: CreateInvoiceReq):
    req = {
        "paymentAmount": body.paymentAmount,
        "merchantOrderId": body.merchantOrderId,
        "productDetails": body.productDetails,
        "email": body.email,
        "callbackUrl": body.callbackUrl,
        "returnUrl": body.returnUrl
    }
    result = duitku.invoice.create(req)
    return result.message

class PaymentMethodReq(BaseModel):
    amount: str
    datetime: str

@app.post("/payment-method")
def get_payment_method(body: PaymentMethodReq):
    req = {
        "amount": body.amount,
        "datetime": body.datetime
    }
    result = duitku.payment.get_methods(req)
    return result.message

class CreateTransactioneReq(BaseModel):
    paymentAmount: int
    merchantOrderId: str
    productDetails: str
    email: str
    customerName: str
    callbackUrl: str
    returnUrl: str

@app.post("/transaction")
def create_transaction(body: CreateTransactioneReq):
    req = {
        "paymentAmount": body.paymentAmount,
        "merchantOrderId": body.merchantOrderId,
        "productDetails": body.productDetails,
        "email": body.email,
        "paymentMethod": "VC",
        "customerVaName": body.customerName,
        "callbackUrl": body.callbackUrl,
        "returnUrl": body.returnUrl
    }
    result = duitku.transaction.create(req)
    return result.message

@app.get("/transaction/{id}")
def get_transaction(id):
    req = {
        "merchantOrderId": id
    }
    result = duitku.transaction.get_status(req)
    return result.message