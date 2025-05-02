from dataclasses import dataclass
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
class OvoPaymentDetails:
    paymentType: str
    amount: int

@dataclass
class Ovo:
    paymentDetails: List[OvoPaymentDetails]

@dataclass
class Shopee:
    promo_ids: str
    useCoin: str

@dataclass
class AccountLink:
    credentialCode: str
    ovo: Ovo
    shopee: Shopee

@dataclass
class CreditCardDetail:
    acquirer: str
    binWhitelist: List[str]

@dataclass
class CreateTransactionRequest:
    merchantCode: str
    paymentAmount: int
    merchantOrderId: str
    productDetails: str
    email: str
    paymentMethod: str
    customerVaName: str
    returnUrl: str
    callbackUrl: str
    signature: str
    accountLink: AccountLink
    creditCardDetail: CreditCardDetail
    additionalParam: Optional[str] = None
    merchantUserInfo: Optional[str] = None
    phoneNumber: Optional[str] = None
    itemDetails: Optional[List[ItemDetails]] = None
    customerDetail: Optional[CustomerDetail] = None
    expiryPeriod: Optional[int] = None

@dataclass
class CreateTransactionResponse:
    merchantCode: str
    reference: str
    paymentUrl: str
    vaNumber: str
    amount: str
    qrString: str

@dataclass
class GetTransactionStatusRequest():
    merchantCode: str
    merchantOrderId: str
    signature: str

@dataclass
class GetTransactionStatusResponse():
    merchantOrderId: str
    reference: str
    amount: str
    fee: str
    statusCode: str
    statusMessage: str