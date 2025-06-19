# University Staff & Student Management System
import re


class Person:
    total_persons = 0

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        Person.total_persons += 1

    def __str__(self):
        return (f"Person's Details: \nPerson Name: {self.name} \n"
                f"Person Email: {self.email} \nPerson Age: {self.age}")

    @classmethod
    def from_string(cls, string):
        name, age, email = string.strip().split(",")
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.fullmatch(pattern, email):
            return cls(name, email, int(age))
        else:
            print("Oops! The email provided is not valid.")
            return None

    @classmethod
    def total_person_count(cls):
        print(f"The total persons including staff and students are: {cls.total_persons} including "
              f"{Student.total_students} students and {Staff.total_staff} staff.")
        return cls.total_persons


class Student(Person):
    total_students = 0
    all_students = []

    def __init__(self, name, email, age, roll_number, course):
        super().__init__(name, email, age)
        self.roll_number = roll_number
        self.course = course
        Student.total_students += 1
        Student.all_students.append(self)

    def __str__(self):
        return str(super().__str__() + (f"\nStudent Roll Number: {self.roll_number} \n"
                                        f"Student Course: {self.course}")).replace("Person", "Student")

    @classmethod
    def from_string(cls, string):
        name, age, email, roll_number, course = string.strip().split(",")
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.fullmatch(pattern, email):
            if cls.validate_roll_number(roll_number):
                return cls(name, email, int(age), roll_number, course)
            else:
                print("Oops! The roll_number you have provided is not valid.")
                return None
        else:
            print("Oops! The email you have provided is not valid.")
            return None

    @staticmethod
    def validate_roll_number(roll_number):
        pattern = r'^[0-9]{6}$'
        if re.fullmatch(pattern, roll_number):
            print("The roll number is valid.")
            return True
        else:
            print("Oops! The roll number is not valid.")
            return False

    @classmethod
    def display_all_students(cls):
        if cls.all_students:
            print("All Student's Details: ")
            print("--" * 30)
            for no, student in enumerate(cls.all_students, start=1):
                print(f"Student {no}:")
                print(student)
                print("--" * 30)
        else:
            print("There are no students to show.")


class Staff(Person):
    total_staff = 0
    all_staff = []

    def __init__(self, name, email, age, emp_id, department):
        super().__init__(name, email, age)
        self.emp_id = emp_id
        self.department = department
        Staff.total_staff += 1
        Staff.all_staff.append(self)

    def __str__(self):
        return str(super().__str__() + (f"\nStaff Employee ID: {self.emp_id} \n"
                                        f"Staff Department: {self.department}")).replace("Person", "Staff")

    @classmethod
    def from_string(cls, string):
        name, age, email, emp_id, department = string.strip().split(",")
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.fullmatch(pattern, email):
            if cls.valid_emp_id(emp_id):
                return cls(name, email, int(age), emp_id, department)
            else:
                print("Oops! The Employee ID you have provided is not valid.")
                return None
        else:
            print("Oops! The email you have provided is not valid.")
            return None

    @staticmethod
    def valid_emp_id(emp_id):
        pattern = r'^[0-9]{6}$'
        if re.fullmatch(pattern, emp_id):
            print("The Employee ID is valid.")
            return True
        else:
            print("Oops! The Employee ID is not valid.")
            return False

    @classmethod
    def display_all_staff(cls):
        if cls.all_staff:
            print("All Staff's Details: ")
            print("--" * 30)
            for no, staff in enumerate(cls.all_staff, start=1):
                print(f"Staff {no}:")
                print(staff)
                print("--" * 30)
        else:
            print("There is no staff to show.")


if __name__ == "__main__":
    student1 = Student("Ali", "ali1@gmail.com", 19, "123456", "Physics")
    student2 = Student.from_string("Hassan,20,hassan2@gmail.com,789012,Chemistry")
    staff1 = Staff("Sohail", "sohail3@gmail.com", 21, "345678", "IT")
    staff2 = Staff.from_string("Abbas,22,abbas4@gmail.com,901234,HR")
    print(student1.__dict__)
    print(staff2.__dict__)
    print(Student.__dict__)
    print(Staff.__dict__)
    print(dir(student2))
    print(help(Staff))
    Person.total_person_count()
    Student.display_all_students()
    Staff.display_all_staff()
