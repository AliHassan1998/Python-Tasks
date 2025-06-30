# Online Payment System with Method Overriding

This Python project demonstrates polymorphism and method overriding through a simulated online payment system with Credit Card and PayPal processing.

---

## 🔧 Key Concepts:
- Inheritance (`Payment → CreditCardPayment / PaypalPayment`)
- Method Overriding (`process_payment`)
- Regex validation for card number, CVV, email
- Magic Methods: `__str__`, `__repr__`, `__eq__`, `__len__`
- Class-level tracking of all payments

---

## 💳 Features:
- Create generic, credit card, and PayPal payments
- Validate inputs before processing
- Compare payments using `==`
- Show payment data using `__str__` and `__repr__`
- Count characters in payer’s name using `len()`

---

## 🚀 How to Run:
```bash
python online_payment_system.py

## Sample Output:
Processing a generic payment...
Processing Credit Card Payment for Hassan. 
Card ending in 8765
Processing Paypal Payment for Sohail using email sohail1@gmail.com
Total payments are: 3
Payer: Ali paid amount: 12000$
CreditCardPayment('Hassan', 10000, '1234567890098765', '890')
True
5
