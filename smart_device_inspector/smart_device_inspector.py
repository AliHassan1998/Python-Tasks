# Task: “Smart Device Inspector” using dir(), __dict__, and help()
class Device:
    """Represents a general electronic device"""
    total_devices = 0

    def __init__(self, device_id, brand, price):
        """Represents a device class constructor to initiate Device objects."""
        if Device.validate_device_id(device_id):
            self.device_id = device_id
        else:
            raise ValueError("Error: Oops! Device ID must be non-empty string.")
        if Device.validate_brand(brand):
            self.brand = brand
        else:
            raise ValueError("Error: Oops! Device Brand must be non-empty string.")
        if Device.validate_price(price):
            self.price = price
        else:
            raise ValueError("Error: Oops! Device Price must be a non-negative number.")
        Device.total_devices += 1

    @staticmethod
    def validate_device_id(device_id):
        """Represents Static Method to validate Device ID"""
        if isinstance(device_id, str) and device_id.strip():
            return True
        else:
            return False

    @staticmethod
    def validate_brand(brand):
        """Represents Static Method to validate Device Brand"""
        if isinstance(brand, str) and brand.strip():
            return True
        else:
            return False

    @staticmethod
    def validate_price(price):
        """Represents Static Method to validate Device Price"""
        if isinstance(price, (int, float)) and price >= 0:
            return True
        else:
            return False

    def device_info(self):
        """Represents Instance Method to show device specifications information."""
        return f"""ID: {self.device_id} \nBrand: {self.brand} \nPrice: {self.price}"""

    def apply_discount(self, percent):
        """Represents Instance Method to apply discount."""
        if isinstance(percent, (int, float)) and 0 <= percent <= 100:
            self.price = self.price - ((percent / 100) * self.price)
            return self.price
        else:
            raise ValueError("Error: Oops! Discount Percentage must be between 0 and 100 (numbers).")

    @classmethod
    def from_string(cls, string):
        """Represents Class Method used as Alternative Constructor to construct new Device objects."""
        device_id, brand, price = string.strip().split(",")
        return cls(device_id, brand, float(price))

    def __str__(self):
        return f"""Device's ID: {self.device_id} \nDevice's Brand: {self.brand} \nDevice's Price: {self.price}"""

    def __repr__(self):
        return f"""Device("{self.device_id}", "{self.brand}", {self.price})"""

    def __len__(self):
        return len(self.brand)


class SmartPhone(Device):
    """Represents a Smartphone device"""
    def __init__(self, device_id, brand, price, ram, storage):
        """Represents a SmartPhone class constructor to initiate SmartPhone objects."""
        super().__init__(device_id, brand, price)
        if SmartPhone.validate_ram(ram):
            self.ram = ram
        else:
            raise ValueError("Error: Oops! SmartPhone Ram must be positive integer.")
        if SmartPhone.validate_storage(storage):
            self.storage = storage
        else:
            raise ValueError("Error: Oops! SmartPhone Storage must be positive integer.")

    @staticmethod
    def validate_ram(ram):
        """Represents Static Method to validate SmartPhone Ram"""
        if isinstance(ram, int) and ram > 0:
            return True
        else:
            return False

    @staticmethod
    def validate_storage(storage):
        """Represents Static Method to validate SmartPhone Storage"""
        if isinstance(storage, int) and storage > 0:
            return True
        else:
            return False

    def device_info(self):
        """Represents Instance Method to show SmartPhone specifications information."""
        return super().device_info() + f""" \nRam: {self.ram}GB \nStorage: {self.storage}GB"""

    def install_app(self, app_name):
        """Represents Instance Method for app installation, and it's confirmation in SmartPhones"""
        return f"{app_name} installed successfully in your device {self.brand}: {self.device_id}."

    @classmethod
    def from_string(cls, string):
        """Represents Class Method used as Alternative Constructor to construct new SmartPhone objects."""
        device_id, brand, price, ram, storage = string.strip().split(",")
        return cls(device_id, brand, float(price), int(ram), int(storage))

    def __str__(self):
        return f"""SmartPhone's ID: {self.device_id} \nSmartPhone's Brand: {self.brand} \nSmartPhone's Price: {self.price} \nSmartPhone's Ram: {self.ram}GB \nSmartPhone's Storage: {self.storage}GB"""

    def __repr__(self):
        return f"""SmartPhone("{self.device_id}", "{self.brand}", {self.price}, {self.ram}, {self.storage})"""


if __name__ == "__main__":
    d1 = Device("D101", "Dell", 1500)
    s1 = SmartPhone("S201", "Apple", 2200, 8, 256)
    print(d1.device_info())
    print(s1.device_info())
    print(d1.__dict__)
    print(s1.__dict__)
    print(Device.__dict__)
    print(SmartPhone.__dict__)
    print(dir(d1))
    print(dir(s1))
    print("apply_discount" in dir(s1))
    print("install_app" in dir(s1))
    print("__dict__" in dir(s1))
    print("__str__" in dir(s1))
    help(Device)
    help(SmartPhone)
    help(d1.apply_discount)
    help(s1.install_app)
    print(d1)
    print(s1)
    print(repr(d1))
    print(repr(s1))
    print(len(d1))
    print(len(s1))
    d1.apply_discount(10)
    print(d1.price)
    print(f"The total devices are: {Device.total_devices}")
    Device.from_string("HP01,HP,1000")
    SmartPhone.from_string("S1001,SamSung,1200,16,512")
    print(Device.total_devices)
    print(s1.install_app("Whatsapp"))
