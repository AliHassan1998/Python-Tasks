# "Employee Management System" using Single Inheritance
class Employee:
    total_employees = 0
    all_employees = []

    def __init__(self, name, age, salary):
        self.name = name
        if Employee.validate_age(age):
            self.age = age
        else:
            raise ValueError("Invalid Age. Age must be a greater or equal to 18 integer value.")
        if Employee.validate_salary(salary):
            self.salary = salary
        else:
            raise ValueError("Invalid Salary. Salary must be a non-negative float value.")
        self.email = f"{self.name.strip().lower().replace(' ', '_')}@company.com"
        Employee.total_employees += 1
        Employee.all_employees.append(self)

    @staticmethod
    def validate_age(age):
        if age >= 18:
            return True
        else:
            return False

    @staticmethod
    def validate_salary(salary):
        if salary >= 0:
            return True
        else:
            return False

    def __str__(self):
        return f"Employee's Details:: \nEmployee Name: {self.name} \n" \
               f"Employee Age: {self.age} \nEmployee Salary: {self.salary} \n" \
               f"Employee Email: {self.email}"

    def __repr__(self):
        return f"Employee('{self.name}', {self.age}, {self.salary})"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.name == other.name and self.salary == other.salary
        return NotImplemented

    def __len__(self):
        return len(self.name)

    @classmethod
    def from_string(cls, string):
        try:
            name, age, salary = string.strip().split(",")
            return cls(name, int(age), float(salary))
        except Exception as e:
            print(f"Oops! An error occurred: {e}")

    def annual_salary(self):
        return self.salary * 12

    @classmethod
    def display_all_employees(cls):
        if cls.all_employees:
            print("All Employee's Details: ")
            print("--" * 30)
            for no, employee in enumerate(cls.all_employees, start=1):
                print(f"Employee {no}: ")
                print(employee)
                print("--" * 30)
        else:
            print("Oops! There are no Employees to display")


class Manager(Employee):
    total_managers = 0
    all_managers = []

    def __init__(self, name, age, salary, department, team_size):
        super().__init__(name, age, salary)
        self.department = department
        if Manager.validate_team_size(team_size):
            self.team_size = team_size
        else:
            raise ValueError("Invalid Team Size. Team Size must be a non-negative integer value.")
        Manager.total_managers += 1
        Manager.all_managers.append(self)

    @staticmethod
    def validate_team_size(team_size):
        if team_size >= 0:
            return True
        else:
            return False

    def __str__(self):
        return str(super().__str__() + f" \nEmployee Department: {self.department} \nEmployee Team Size: "
                                       f"{self.team_size} \nSenior Manager: {self.is_senior()}").replace("Employee", "Manager")

    def __repr__(self):
        return f"Manager('{self.name}', {self.age}, {self.salary}, '{self.department}', {self.team_size})"

    def is_senior(self):
        if self.team_size > 5:
            return True
        else:
            return False

    @classmethod
    def from_string(cls, string):
        try:
            name, age, salary, department, team_size = string.strip().split(",")
            return cls(name, int(age), float(salary), department, int(team_size))
        except Exception as e:
            print(f"Oops! An error occurred: {e}")

    def __call__(self, value):
        if not isinstance(value, int):
            raise TypeError("Invalid Type. Team Size Addition must be an integer.")
        elif value < 0:
            raise ValueError("Invalid Value. Team Size Addition must be a non-negative integer value.")
        else:
            self.team_size += value
            return self.team_size

    @classmethod
    def display_all_managers(cls):
        if cls.all_managers:
            print("All Manager's Details: ")
            print("--" * 30)
            for no, manager in enumerate(cls.all_managers, start=1):
                print(f"Manager {no}: ")
                print(manager)
                print("--" * 30)
        else:
            print("Oops! There are no Managers to display.")


if __name__ == "__main__":
    employee1 = Employee("Ali", 26, 30000.0)
    employee2 = Employee.from_string("Hassan,27,35000")
    manager1 = Manager("Sohail", 28, 40000.0, "Medical", 5)
    manager2 = Manager.from_string("Abbas,29,45000,IT,6")
    print(employee1)
    print(repr(employee1))
    print(employee2)
    print(repr(employee2))
    print(manager1)
    print(repr(manager1))
    print(manager2)
    print(repr(manager2))
    print(employee1 == manager1)
    print(f"Annual Salary of Employee: {employee1.name} is {employee1.annual_salary()}")
    print(f"Annual Salary of Employee: {employee2.name} is {Employee.annual_salary(employee2)}")
    print(f"Annual Salary of Manager: {manager1.name} is {Manager.annual_salary(manager1)}")
    print(f"Annual Salary of Manager: {manager2.name} is {manager2.annual_salary()}")
    print(manager1.is_senior())
    print(manager2.is_senior())
    print(len(employee1))
    print(len(employee2))
    print(len(manager1))
    print(len(manager2))
    manager2(4)
    print(manager2)
    print(f"Total Number of Employees are: {Employee.total_employees} out of which {Manager.total_managers}"
          f" are Managers.")
    Employee.display_all_employees()
    Manager.display_all_managers()
