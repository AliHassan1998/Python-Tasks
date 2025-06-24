# Introspection Explorer for a Mini Employee-Manager System
import re


class Employee:
    total_employees = 0
    all_employees = []

    def __init__(self, name, emp_id, email, department):
        self.name = name
        self.emp_id = emp_id
        self.email = email
        self.department = department
        Employee.total_employees += 1
        Employee.all_employees.append(self)

    def __str__(self):
        return (f"Employee's Details: \nEmployee Name: {self.name} \n"
                f"Employee ID: {self.emp_id} \nEmployee Email: {self.email} \n"
                f"Employee Department: {self.department}")

    @classmethod
    def from_string(cls, string):
        name, emp_id, email, department = string.strip().split(",")
        if cls.is_valid_email(email):
            if cls.is_valid_emp_id(emp_id):
                return cls(name, emp_id, email, department)
            else:
                print(f"Error: Enter a valid Employee ID for Employee's registration.")
        else:
            print(f"Error: Enter a valid email for Employee's registration.")

    @staticmethod
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.fullmatch(pattern, email):
            print("The email is valid.")
            return True
        else:
            print("Oops! The email is not valid.")
            return False

    @classmethod
    def all_employees_count(cls):
        return (f"The total employees are: {cls.total_employees} out of which {Manager.total_managers}"
                f" are managers.")

    @staticmethod
    def is_valid_emp_id(emp_id):
        pattern = r'^[0-9]{6}$'
        if re.fullmatch(pattern, emp_id):
            return True
        else:
            return False

    @classmethod
    def all_employees_details(cls):
        if cls.all_employees:
            print("All Employee's Details: ")
            print("--" * 30)
            for no, employee in enumerate(cls.all_employees, start=1):
                print(f"Employee {no}: ")
                print(employee)
                print("--" * 30)
        else:
            print(f"There are no employees to show.")


class Manager(Employee):
    all_managers = []
    total_managers = 0

    def __init__(self, name, emp_id, email, department, team_size, level):
        super().__init__(name, emp_id, email, department)
        self.team_size = team_size
        self.level = level
        Manager.all_managers.append(self)
        Manager.total_managers += 1

    def __str__(self):
        return str(super().__str__() + (f"\nManager's Team Size: {self.team_size} \n"
                                        f"Manager's Level: {self.level}")).replace("Employee", "Manager")

    @classmethod
    def from_string(cls, string):
        name, emp_id, email, department, team_size, level = string.strip().split(",")
        if cls.is_valid_email(email):
            if cls.is_valid_emp_id(emp_id):
                return cls(name, emp_id, email, department, int(team_size), int(level))
            else:
                print(f"Error: Enter a valid Employee ID for Manager's registration.")
        else:
            print(f"Error: Enter a valid email for Manager's registration.")

    @classmethod
    def all_managers_details(cls):
        if cls.all_managers:
            print("All Manager's Details: ")
            print("--" * 30)
            for no, manager in enumerate(cls.all_managers, start=1):
                print(f"Manager {no}: ")
                print(manager)
                print("--" * 30)
        else:
            print(f"There are no managers to show.")


if __name__ == "__main__":
    employee1 = Employee("Ali", "123456", "ali1@gmail.com", "IT")
    employee2 = Employee.from_string("Hassan,789012,hassan2@gmail.com,HR")
    manager1 = Manager("Sohail", "345678", "sohail3@gmail.com", "Medical", 8, 3)
    manager2 = Manager.from_string("Abbas,901234,abbas4@gmail.com,Nursing,10,4")
    print(employee1.__dict__)
    print(manager2.__dict__)
    print(Employee.__dict__)
    print(dir(employee2))
    print(dir(manager1))
    print(dir(Manager))
    print(help(manager2))
    print(help(employee2))
    print(help(Employee))
    print(Employee.all_employees_count())
    print(Employee.all_employees_details())
    print(Manager.all_managers_details())
