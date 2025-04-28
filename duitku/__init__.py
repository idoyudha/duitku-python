from .client import DuitkuClient
from .invoice import InvoiceService

class Duitku():
    def __init__(self):
        self.client = DuitkuClient()
        self.invoice = InvoiceService(self.client)