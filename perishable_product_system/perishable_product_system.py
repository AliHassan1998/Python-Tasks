# Single Inheritance: Product → PerishableProduct
import datetime


class Product:
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price >= 0:
            self._price = float(price)
        else:
            raise ValueError("Error: Oops! Price must be a non-negative float value.")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self._quantity = quantity
        else:
            raise ValueError("Error: Oops! Quantity must be a non-negative integer value.")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print("The Product Quantity has been updated successfully!")

    def apply_discount(self, discount_percentage):
        if isinstance(discount_percentage, (int, float)) and 0 <= discount_percentage <= 100:
            discount = (discount_percentage / 100) * self.price
            self.price -= discount
            print(f"Applied {discount_percentage}% discount to {self.product_id}. New Price: ${self.price}")
            return self.price
        else:
            raise ValueError("Error: Oops! Discount Percentage must be between 0 and 100, integer or float value.")

    @classmethod
    def from_string(cls, string):
        try:
            product_id, name, price, quantity = string.strip().split(",")
            return cls(product_id, name, float(price), int(quantity))
        except Exception as ex:
            print(f"Error: {ex}")

    def __str__(self):
        return f"Product ({self.product_id}: {self.name} -- ${self.price} (qty: {self.quantity}))"

    def display_details(self):
        return f"Product's Details: \nProduct's ID: {self.product_id} \nProduct's Name: {self.name} \n" \
               f"Product's Price: {self.price} \nProduct's Quantity: {self.quantity}"


class PerishableProduct(Product):
    def __init__(self, product_id, name, price, quantity, expiry_date: str):
        super().__init__(product_id, name, price, quantity)
        self.expiry_date = expiry_date

    @staticmethod
    def validate_date(date):
        if isinstance(date, datetime.date):
            return date
        elif isinstance(date, str):
            try:
                date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
                return date
            except ValueError:
                raise ValueError("Error: Oops! Invalid Date Format. Must be 'YYYY-MM-DD'")
        else:
            raise ValueError("Error: Oops! Date must be in datetime.date or 'YYYY-MM-DD' string format.")

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        self._expiry_date = PerishableProduct.validate_date(expiry_date)

    def is_expired(self, current_date):
        return PerishableProduct.validate_date(current_date) > self.expiry_date

    def days_until_expiry(self, current_date):
        return (self.expiry_date - PerishableProduct.validate_date(current_date)).days

    def reduce_price_if_near_expiry(self, current_date, days_threshold, reduction_percentage):
        try:
            if 0 <= self.days_until_expiry(current_date) <= days_threshold:
                self.price = self.apply_discount(reduction_percentage)
                print(f"{self.name} is within {days_threshold} day of expiry"
                      f" ({self.days_until_expiry(current_date)} days left). Applied {reduction_percentage}% reduction."
                      f" New Price: ${self.price}")
                return self.price
            elif self.days_until_expiry(current_date) < 0:
                self.price = 0.0
                print(f"{self.name} is already expired. Its price is now: ${self.price}.")
                return self.price
        except Exception as exe:
            print(f"Error: {exe}")

    def display_details(self):
        return str(super().display_details() + f"\nProduct Expiry Date: {self.expiry_date} \n"
                                               f"Product Days until Expiry: {self.days_until_expiry(datetime.date.today())} \n"
                                               f"Is Expired: {self.is_expired(datetime.date.today())}").replace("Product", "Perishable Product")

    def __str__(self):
        return str(super().__str__() + f", (Expiry Date: {self.expiry_date})").replace("Product", "Perishable Product")

    @classmethod
    def from_string(cls, string):
        try:
            product_id, name, price, quantity, expiry_date = string.strip().split(",")
            return cls(product_id, name, float(price), int(quantity), expiry_date)
        except Exception as execp:
            print(f"Error: {execp}")


if __name__ == "__main__":
    try:
        product1 = Product("P001", "NoteBook", 10.0, 50)
        product2 = Product.from_string("P002,Pencils,4.0,100")
        perishable_product1 = PerishableProduct("PP003", "Milk", 20.0, 150, "2025-08-14")
        perishable_product2 = PerishableProduct.from_string("PP004,Yogurt,15.0,200,2025-08-20")
        today_current_date = "2025-08-12"
        print(product1.display_details())
        print(product2.display_details())
        print(perishable_product1.display_details())
        print(perishable_product2.display_details())
        print(product1)
        print(product2)
        print(perishable_product1)
        print(perishable_product2)
        product1.apply_discount(10)
        print(product1.display_details())
        perishable_product1.reduce_price_if_near_expiry(today_current_date, days_threshold=3, reduction_percentage=30)
        print(perishable_product1.display_details())
        print(perishable_product1.is_expired("2025-08-16"))
        print(perishable_product2.is_expired("2025-08-22"))
    except Exception as e:
        print(f"{e}")
