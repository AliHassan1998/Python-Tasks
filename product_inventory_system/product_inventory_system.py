# Operator Overloading in a “Product Inventory System”
class Product:
    total_products = 0
    all_products = []

    def __init__(self, name, price, quantity):
        if Product.validate_name(name):
            self.name = name
        else:
            raise ValueError("Product Name can't be empty.")
        if Product.validate_price(price):
            self.price = price
        else:
            raise ValueError("Product Price must be Non Negative Float")
        if Product.validate_quantity(quantity):
            self.quantity = quantity
        else:
            raise ValueError("Product Quantity must be a Positive Integer.")
        Product.total_products += 1
        Product.all_products.append(self)

    @staticmethod
    def validate_name(name):
        if name:
            return True
        else:
            return False

    @staticmethod
    def validate_price(price):
        if price >= 0:
            return True
        else:
            return False

    @staticmethod
    def validate_quantity(quantity):
        if quantity > 0:
            return True
        else:
            return False

    def __str__(self):
        return f"Product's Details: \nProduct Name: {self.name.title()} \nProduct Price: {self.price} \n" \
               f"Product Quantity: {self.quantity}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if isinstance(other, Product):
            if self.name.lower() == other.name.lower():
                return Product(self.name, self.price + other.price, self.quantity + other.quantity)
            else:
                raise ValueError(f"Product {self.name} and Product {other.name} can't be added.")
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            if other < 0:
                raise ValueError(f"Can't Multiply Quantity by a negative number {other}.")
            else:
                return Product(self.name, self.price, self.quantity * other)
        elif isinstance(other, float):
            if not 0 < other < 1:
                raise ValueError("To apply Discount, value must be between 0 and 1.")
            else:
                return Product(self.name, self.price * other, self.quantity)
        else:
            raise TypeError(f"Unsupported Operand: {other}")

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name.lower() == other.name.lower() and self.price == other.price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price > other.price
        return NotImplemented

    def __len__(self):
        return len(self.name)

    def __call__(self, value):
        if not isinstance(value, int):
            raise TypeError("Product Restock Quantity must be an integer.")
        elif value < 0:
            raise ValueError("Product Restock Quantity must be Non Negative.")
        else:
            self.quantity = self.quantity + value
            return self.quantity

    @classmethod
    def from_string(cls, string):
        name, price, quantity = string.strip().split(",")
        return cls(name, float(price), int(quantity))

    @classmethod
    def display_all_products(cls):
        if cls.all_products:
            print("All Product's Details: ")
            print("--" * 30)
            for no, product in enumerate(cls.all_products, start=1):
                print(f"Product {no}: ")
                print(product)
                print("--" * 30)
        else:
            print("There are no Products to display.")


if __name__ == "__main__":
    p1 = Product("Notebook", 5.0, 10)
    p2 = Product.from_string("Notebook,3.0,20")
    print(p1)
    print(repr(p1))
    print(p2)
    print(repr(p2))
    p3 = p1 + p2
    print(p3)
    print(repr(p3))
    p4 = p3 * 0.5
    print(p4)
    print(repr(p4))
    p5 = p4 * 2
    print(p5)
    print(repr(p5))
    print(p1 == p2)
    print(p1 < p2)
    print(len(p1))
    p1(5)
    print(p1)
    print(f"The total numbers of Products are: {Product.total_products}")
    Product.display_all_products()
