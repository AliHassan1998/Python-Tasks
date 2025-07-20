# Employee Payroll System with Method Overriding
class Employee:
    def __init__(self, name, emp_id, base_pay):
        self.name = name
        self.emp_id = emp_id
        if Employee.validate_base_pay(base_pay):
            self.base_pay = base_pay
        else:
            raise ValueError("Error: Base Pay can't be negative.")

    @staticmethod
    def validate_base_pay(base_pay):
        if base_pay >= 0:
            return True
        else:
            return False

    def __str__(self):
        return (f"Employee's Details: \nEmployee's Name: {self.name} \n"
                f"Employee's ID: {self.emp_id} \nEmployee's Total Salary: {self.calculate_salary()}")

    def __repr__(self):
        return f"Employee('{self.name}', '{self.emp_id}', {self.base_pay})"

    def calculate_salary(self):
        return self.base_pay

    @classmethod
    def from_string(cls, string):
        name, emp_id, base_pay = string.strip().split(",")
        return cls(name, emp_id, int(base_pay))


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_pay, bonus=None):
        super().__init__(name, emp_id, base_pay)
        if bonus is None:
            self.bonus = 0
        else:
            if FullTimeEmployee.validate_bonus(bonus):
                self.bonus = bonus
            else:
                raise ValueError("Error: Bonus can't be negative.")

    @staticmethod
    def validate_bonus(bonus):
        if bonus >= 0:
            return True
        else:
            return False

    def calculate_salary(self):
        return self.base_pay + self.bonus

    def __str__(self):
        return str(super().__str__() + f" (Base = {self.base_pay} + Bonus = {self.bonus})"
                                       f"").replace("Employee", "Full Time Employee")

    def __repr__(self):
        return f"FullTimeEmployee('{self.name}', '{self.emp_id}', {self.base_pay}, {self.bonus})"

    @classmethod
    def from_string(cls, string):
        name, emp_id, base_pay, bonus = string.strip().split(",")
        return cls(name, emp_id, int(base_pay), int(bonus))


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_pay, hours_worked, hourly_rate):
        super().__init__(name, emp_id, base_pay)
        if PartTimeEmployee.validate_hours_worked(hours_worked):
            self.hours_worked = hours_worked
        else:
            raise ValueError("Error: Number of hours worked can't be negative.")
        if PartTimeEmployee.validate_hourly_rate(hourly_rate):
            self.hourly_rate = hourly_rate
        else:
            raise ValueError("Error: Hourly rate can't be negative.")

    @staticmethod
    def validate_hours_worked(hours_worked):
        if hours_worked >= 0:
            return True
        else:
            return False

    @staticmethod
    def validate_hourly_rate(hourly_rate):
        if hourly_rate >= 0:
            return True
        else:
            return False

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

    def __str__(self):
        return str(super().__str__() + f" (Numbers of Hours * Hourly Rate = {self.hours_worked} "
                                       f"* {self.hourly_rate} = {self.calculate_salary()})"
                                       f"").replace("Employee", "Part Time Employee")

    def __repr__(self):
        return f"PartTimeEmployee('{self.name}', '{self.emp_id}', {self.base_pay}," \
               f" {self.hours_worked}, {self.hourly_rate})"

    @classmethod
    def from_string(cls, string):
        name, emp_id, base_pay, hours_worked, hourly_rate = string.strip().split(",")
        return cls(name, emp_id, int(base_pay), int(hours_worked), int(hourly_rate))


if __name__ == "__main__":
    employee1 = Employee("Ali", "EM101", 10000)
    employee2 = Employee.from_string("Hassan,EM202,12000")
    full_time_employee1 = FullTimeEmployee("Sohail", "FT303", 14000, 1000)
    full_time_employee2 = FullTimeEmployee.from_string("Abbas,FT404,16000,3000")
    part_time_employee1 = PartTimeEmployee("Zaheer", "PT505", 18000, 160, 35)
    part_time_employee2 = PartTimeEmployee.from_string("Asif,PT606,20000,140,40")
    print(employee1.calculate_salary())
    print(employee2.calculate_salary())
    print(full_time_employee1.calculate_salary())
    print(full_time_employee2.calculate_salary())
    print(part_time_employee1.calculate_salary())
    print(part_time_employee2.calculate_salary())
    print(employee1)
    print(repr(employee2))
    print(full_time_employee2)
    print(repr(full_time_employee1))
    print(part_time_employee1)
    print(repr(part_time_employee2))
