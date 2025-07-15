# Shopping Cart System with Operator Overloading
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        if price >= 0:
            self.price = price
            if quantity >= 0:
                self.quantity = quantity
            else:
                raise ValueError(f"Oops! The Product Quantity can't be negative: {quantity}.")
        else:
            raise ValueError(f"Oops! The Product Price can't be negative: {price}.")

    def __str__(self):
        return f"Product's Details: \nProduct Name: {self.name} \n" \
               f"Product Price: {self.price} \nProduct Quantity: {self.quantity}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name.lower() == other.name.lower()
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Product):
            if self == other:
                return Product(self.name, (self.price + other.price) / 2, self.quantity + other.quantity)
            else:
                raise ValueError("Products with different names can't be added.")
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented

    @classmethod
    def from_string(cls, string):
        name, price, quantity = string.strip().split(",")
        return cls(name, int(price), int(quantity))


class Cart:
    def __init__(self, all_products=None):
        if all_products is None:
            self.all_products = []
        else:
            self.all_products = all_products

    def total_price(self):
        total_price = 0
        for product in self.all_products:
            total_price += product.price * product.quantity
        return total_price

    def __len__(self):
        products_set = set(product.name.lower() for product in self.all_products)
        return len(products_set)

    def __contains__(self, new_product):
        return any(product == new_product for product in self.all_products)

    def __str__(self):
        product_lines = "\n".join(f"{i}: {p}" for i, p in enumerate(self.all_products, start=1))
        return f"Cart's Details:\nNumber of Products: {len(self)}\nProducts:\n{product_lines}"

    def __repr__(self):
        return f"Cart({self.all_products})"

    def __add__(self, other):
        if isinstance(other, Cart):
            merged_cart = Cart()
            for product in self.all_products + other.all_products:
                merged_cart.add_product(product)
            return merged_cart
        elif isinstance(other, Product):
            new_cart = Cart(self.all_products.copy())
            new_cart.add_product(other)
            return new_cart
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Cart):
            return self.total_price() == other.total_price()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Cart):
            return self.total_price() > other.total_price()
        return NotImplemented

    def remove_product(self, product):
        if product in self.all_products:
            self.all_products.remove(product)
            print("The product is successfully removed!")
        else:
            print("The product is not in the cart.")

    def add_product(self, new_product):
        for i, existing in enumerate(self.all_products):
            if existing == new_product:
                self.all_products[i] = existing + new_product
                return
        self.all_products.append(new_product)


if __name__ == "__main__":
    product1 = Product("Laptop", 1000, 1)
    product2 = Product.from_string("Laptop,1200,2")
    product3 = Product("Mouse", 50, 1)
    print(product1)
    print(product2)
    print(product3)
    combined = product1 + product2
    print(combined)
    print(product1 == product2)
    print(product1 < product3)
    cart1 = Cart([product1, product3])
    cart2 = Cart([product2])
    print(cart1)
    print(cart2)
    cart3 = cart1 + cart2
    print(cart3)
    print(len(cart3))
    print(cart3.total_price())
    print(cart1 == cart2)
    print(cart3 > cart2)
    print(product3 in cart3)
    print(repr(product1))
    print(repr(cart3))
    another_product = Product("Chocolate", 120, 5)
    cart3.add_product(another_product)
    print(cart3)
    cart3.remove_product(another_product)
    print(cart3)
