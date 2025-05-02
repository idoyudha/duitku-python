from dataclasses import dataclass
from typing import List

@dataclass
class GetPaymentMethodRequest:
    merchantCode: str
    amount: int
    datetime: str
    signature: str

@dataclass
class PaymentFee:
    paymentMethod: str
    paymentName: str
    paymentImage: str
    totalFee: str

@dataclass
class GetPaymentMethodResponse:
    paymentFee: List[PaymentFee]
    responseCode: str
    responseMessage: str