from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(Payment):

    def pay(self):
        print("success: CreditCardPayment")

class PayPalPayment(Payment):

    def pay(self):
        print("success: PayPalPayment")

class CryptoPayment(Payment):
    def pay(self):
        print("success: CryptoPayment")