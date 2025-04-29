from .client import DuitkuClient
from .invoice import InvoiceService
from .payment import PaymentService

class Duitku():
    def __init__(self):
        self.client = DuitkuClient()
        self.invoice = InvoiceService(self.client)
        self.payment = PaymentService(self.client)