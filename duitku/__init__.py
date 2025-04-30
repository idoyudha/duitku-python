from .client import DuitkuClient
from .invoice import InvoiceService
from .payment import PaymentService
from .transaction import TransactionService

class Duitku:
    def __init__(self):
        """
        Initialize Duitku object.

        Initialize Duitku object by creating its client,
        invoice, payment, and transaction services.

        :return: None
        """
        self.client = DuitkuClient()
        self.invoice = InvoiceService(self.client)
        self.payment = PaymentService(self.client)
        self.transaction = TransactionService(self.client)