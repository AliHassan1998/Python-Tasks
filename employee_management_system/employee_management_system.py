# Employee Management System with Method Overriding
import re


class Employee:
    total_employees = 0
    all_employees = []

    def __init__(self, name, email, salary):
        self.name = name
        self.salary = salary
        if Employee.is_valid_email(email):
            self.email = email
            Employee.total_employees += 1
            Employee.all_employees.append(self)
        else:
            raise ValueError("The Entered Employee Email is not valid.")

    @staticmethod
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.fullmatch(pattern, email):
            return True
        else:
            return False

    def __str__(self):
        return (f"Employee's Details: \nEmployee Name: {self.name} \n"
                f"Employee Email: {self.email} \nEmployee Salary: {self.salary}")

    def __repr__(self):
        return f"Employee('{self.name}', '{self.email}', {self.salary})"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.email == other.email
        return NotImplemented

    def __len__(self):
        return len(self.name)

    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.salary > other.salary
        return NotImplemented

    def work(self):
        return f"Employee: {self.name} is working."

    @classmethod
    def from_string(cls, string):
        name, email, salary = string.strip().split(",")
        return cls(name, email, int(salary))

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
            print("Oops! There are no Employees to display.")


class Developer(Employee):
    total_developers = 0
    all_developers = []

    def __init__(self, name, email, salary, programming_language):
        super().__init__(name, email, salary)
        self.programming_language = programming_language
        Developer.total_developers += 1
        Developer.all_developers.append(self)

    def work(self):
        return f"Developer: {self.name} is coding in {self.programming_language}."

    @classmethod
    def from_string(cls, string):
        name, email, salary, programming_language = string.strip().split(",")
        return cls(name, email, int(salary), programming_language)

    def __str__(self):
        return str(super().__str__() + f"\nDeveloper Programming Language: {self.programming_language}").replace("Employee", "Developer")

    def __repr__(self):
        return f"Developer('{self.name}', '{self.email}', {self.salary}, '{self.programming_language}')"


class Manager(Employee):
    total_managers = 0
    all_managers = []

    def __init__(self, name, email, salary, team_size):
        super().__init__(name, email, salary)
        self.team_size = team_size
        Manager.total_managers += 1
        Manager.all_managers.append(self)

    def work(self):
        return f"Manager: {self.name} is managing a team of {self.team_size} people."

    @classmethod
    def from_string(cls, string):
        name, email, salary, team_size = string.strip().split(",")
        return cls(name, email, int(salary), int(team_size))

    def __str__(self):
        return str(super().__str__() + f"\nManager Team Size: {self.team_size}").replace("Employee", "Manager")

    def __repr__(self):
        return f"Manager('{self.name}', '{self.email}', {self.salary}, {self.team_size})"


if __name__ == "__main__":
    employee1 = Employee("Ali", "ali1@gmail.com", 10000)
    employee2 = Employee.from_string("Hassan,hassan2@gmail.com,12000")
    developer1 = Developer("Sohail", "sohail3@gmail.com", 14000, "Python")
    developer2 = Developer.from_string("Abbas,abbas4@gmail.com,16000,Java")
    manager1 = Manager("Zaheer", "zaheer5@gmail.com", 18000, 5)
    manager2 = Manager.from_string("Asif,asif6@gmail.com,20000,10")
    print(employee1)
    print(employee2)
    print(developer1)
    print(developer2)
    print(manager1)
    print(manager2)
    print(employee1.work())
    print(employee2.work())
    print(developer1.work())
    print(developer2.work())
    print(manager1.work())
    print(manager2.work())
    print(f"Total Employees are: {Employee.total_employees} out of which there are {Developer.total_developers} "
          f"developers and {Manager.total_managers} managers.")
    Employee.display_all_employees()
    print(repr(employee1))
    print(repr(developer2))
    print(repr(manager1))
    print(employee1 == developer2)
    print(len(manager2))
    print(manager2 > developer1)
