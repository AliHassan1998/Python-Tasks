# Vehicle Registration System
import re


class Vehicle:
    total_vehicles = 0
    all_vehicles = []

    def __init__(self, owner, license_plate, vehicle_type):
        self.owner = owner
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        Vehicle.total_vehicles += 1
        Vehicle.all_vehicles.append(self)

    @staticmethod
    def is_valid_license_plate(license_plate):
        pattern = r'^[A-Za-z]{3}-\d{4}$'
        if re.fullmatch(pattern, license_plate):
            print("The License Plate is valid.")
            return True
        else:
            print("The License Plate is not valid.")
            return False

    def __str__(self):
        return (f"Vehicle's Details: \nVehicle Owner: {self.owner} \n"
                f"Vehicle's License Plate: {self.license_plate} \nVehicle's Type: {self.vehicle_type}")

    @classmethod
    def from_string(cls, string):
        try:
            owner, license_plate, vehicle_type = string.strip().split(",")
            if cls.is_valid_license_plate(license_plate):
                return cls(owner, license_plate, vehicle_type)
            else:
                print("Oops! The entered Vehicle's License Plate is not valid.")
        except Exception as e:
            print(f"Error: {e}.")
            return None

    @classmethod
    def display_all_vehicles(cls):
        if cls.all_vehicles:
            print("All Vehicle's Details: ")
            print("--" * 30)
            for no, vehicle in enumerate(cls.all_vehicles, start=1):
                print(f"Vehicle {no}: ")
                print(vehicle)
                print("--" * 30)
        else:
            print("There are no Vehicles to show.")


class Car(Vehicle):
    total_cars = 0
    all_cars = []

    def __init__(self, owner, license_plate, vehicle_type, brand, seats):
        super().__init__(owner, license_plate, vehicle_type)
        self.brand = brand
        self.seats = seats
        Car.total_cars += 1
        Car.all_cars.append(self)

    def __str__(self):
        return str(super().__str__() + (f" \nCar's Brand: {self.brand} \n"
                                        f"Car's Seats: {self.seats}")).replace("Vehicle", "Car")

    @classmethod
    def from_string(cls, string):
        try:
            owner, license_plate, vehicle_type, brand, seats = string.strip().split(",")
            if cls.is_valid_license_plate(license_plate):
                return cls(owner, license_plate, vehicle_type, brand, int(seats))
            else:
                print("Oops! The entered Car's License Plate is not valid.")
        except Exception as e:
            print(f"Error: {e}.")
            return None

    @classmethod
    def display_all_cars(cls):
        if cls.all_cars:
            print("All Car's Details: ")
            print("--" * 30)
            for no, car in enumerate(cls.all_cars, start=1):
                print(f"Car {no}: ")
                print(car)
                print("--" * 30)
        else:
            print("There are no cars to show.")


class ElectricCar(Car):
    total_electric_cars = 0
    all_electric_cars = []

    def __init__(self, owner, license_plate, vehicle_type, brand, seats, battery_range, charging_time):
        super().__init__(owner, license_plate, vehicle_type, brand, seats)
        self.battery_range = battery_range
        self.charging_time = charging_time
        ElectricCar.total_electric_cars += 1
        ElectricCar.all_electric_cars.append(self)

    def __str__(self):
        return str(super().__str__() + (f" \nElectric Car's Battery Range: {self.battery_range} \n"
                                        f"Electric Car's Charging Time: {self.charging_time}")).replace("Car", "Electric Car")

    @classmethod
    def from_string(cls, string):
        try:
            owner, license_plate, vehicle_type, brand, seats, battery_range, charging_time = string.strip().split(",")
            if cls.is_valid_license_plate(license_plate):
                return cls(owner, license_plate, vehicle_type, brand, int(seats), battery_range, charging_time)
            else:
                print("Oops! The entered Electric Car's License Plate is not valid.")
        except Exception as e:
            print(f"Error: {e}.")
            return None

    @classmethod
    def display_all_electric_cars(cls):
        if cls.all_electric_cars:
            print("All Electric Car's Details: ")
            print("--" * 30)
            for no, electric_car in enumerate(cls.all_electric_cars, start=1):
                print(f"Electric Car {no}: ")
                print(electric_car)
                print("--" * 30)
        else:
            print("There are no Electric Cars to show.")


if __name__ == "__main__":
    vehicle1 = Vehicle.from_string("Ali,CDB-4321,Suzuki")
    car1 = Car.from_string("Hassan,ABC-1234,Sedan,Toyota,5")
    ev1 = ElectricCar.from_string("Sara,XYZ-5678,SUV,Tesla,5,400km,1hr")
    print(f"Total Vehicles are: {Vehicle.total_vehicles}")
    Vehicle.is_valid_license_plate("BB-234")
    Vehicle.display_all_vehicles()
    print(f"Total Cars are: {Car.total_cars}")
    Car.display_all_cars()
    print(f"Total Electric Cars: {ElectricCar.total_electric_cars}")
    ElectricCar.display_all_electric_cars()
    print(ev1.__dict__)
    print(Car.__dict__)
    print(dir(vehicle1))
    print(dir(ElectricCar))
    print(help(Car))
