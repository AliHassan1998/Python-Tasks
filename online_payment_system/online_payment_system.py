# Online Payment System with Method Overriding
import re


class Payment:
    total_payments = 0
    all_payments = []

    def __init__(self, payer_name, amount):
        self.payer_name = payer_name
        self.amount = amount
        Payment.total_payments += 1
        Payment.all_payments.append(self)

    def process_payment(self):
        return f"Processing a generic payment..."  # Will be overridden

    def __str__(self):
        return f"Payer: {self.payer_name} paid amount: {self.amount}$"

    def __repr__(self):
        return f"Payment('{self.payer_name}', {self.amount})"

    def __eq__(self, other):
        if isinstance(other, Payment):
            return self.amount == other.amount
        return NotImplemented

    def __len__(self):
        return len(self.payer_name)

    @classmethod
    def display_all_payments(cls):
        if cls.all_payments:
            print("All Payment Details: ")
            print("--" * 30)
            for no, payment in enumerate(cls.all_payments, start=1):
                print(f"Payment {no}: ")
                print(payment)
                print("--" * 30)
        else:
            print("Oops! There are no payments to show.")


class CreditCardPayment(Payment):
    def __init__(self, payer_name, amount, card_number, cvv):
        super().__init__(payer_name, amount)
        if CreditCardPayment.is_valid_card_number(card_number):
            self.card_number = card_number
            if CreditCardPayment.is_valid_cvv(cvv):
                self.cvv = cvv
            else:
                raise ValueError(f"Invalid CVV: {cvv}")
        else:
            raise ValueError(f"Invalid Card Number: {card_number}.")

    def process_payment(self):
        return (f"Processing Credit Card Payment for {self.payer_name}. \n"
                f"Card ending in {self.card_number[-4:]}")

    @staticmethod
    def is_valid_card_number(card_number):
        pattern = r'^[0-9]{16}$'
        if re.fullmatch(pattern, card_number):
            return True
        else:
            return False

    @staticmethod
    def is_valid_cvv(cvv):
        pattern = r'^\d{3}$'
        if re.fullmatch(pattern, cvv):
            return True
        else:
            return False

    def __repr__(self):
        return f"CreditCardPayment('{self.payer_name}', {self.amount}, '{self.card_number}', '{self.cvv}')"


class PaypalPayment(Payment):
    def __init__(self, payer_name, amount, paypal_email):
        super().__init__(payer_name, amount)
        if PaypalPayment.is_valid_paypal_email(paypal_email):
            self.paypal_email = paypal_email
        else:
            raise ValueError(f"Invalid Paypal Email: {paypal_email}")

    def process_payment(self):
        return f"Processing Paypal Payment for {self.payer_name} using email {self.paypal_email}"

    @classmethod
    def is_valid_paypal_email(cls, paypal_email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.fullmatch(pattern, paypal_email):
            return True
        else:
            return False

    def __repr__(self):
        return f"PaypalPayment('{self.payer_name}', {self.amount}, '{self.paypal_email}')"


if __name__ == "__main__":
    payment1 = Payment("Ali", 12000)
    credit_card_payment1 = CreditCardPayment("Hassan", 10000, "1234567890098765", "890")
    paypal_payment1 = PaypalPayment("Sohail", 15000, "sohail1@gmail.com")
    print(payment1.process_payment())
    print(credit_card_payment1.process_payment())
    print(paypal_payment1.process_payment())
    print(f"Total payments are: {Payment.total_payments}")
    Payment.display_all_payments()
    print(payment1)
    print(credit_card_payment1)
    print(paypal_payment1)
    print(payment1 == credit_card_payment1)
    print(len(paypal_payment1))
    print(repr(payment1))
    print(repr(credit_card_payment1))
    print(repr(paypal_payment1))
