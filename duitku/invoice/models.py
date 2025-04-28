from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ItemDetails:
    name: str
    quantity: int
    price: int

@dataclass
class CustomerDetail:
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    phoneNumber: Optional[str] = None

@dataclass
class CreditCardDetail:
    acquirer: str
    binWhitelist: List[str]

@dataclass
class CreateInvoiceRequest:
    paymentAmount: int
    merchantOrderId: str
    productDetails: str
    email: str
    additionalParam: Optional[str] = None
    merchantUserInfo: Optional[str] = None
    customerVaName: str = ''
    phoneNumber: Optional[str] = None
    itemDetails: Optional[List[ItemDetails]] = field(default_factory=list)
    customerDetail: Optional[CustomerDetail] = None
    callbackUrl: str = ''
    returnUrl: str = ''
    expiryPeriod: Optional[int] = None
    paymentMethod: str = ''
    creditCardDetail: Optional[CreditCardDetail] = None

@dataclass
class CreateInvoiceResponse:
    merchantCode: str
    reference: str
    paymentUrl: str
    amount: str
    statusCode: str
    statusMessage: str