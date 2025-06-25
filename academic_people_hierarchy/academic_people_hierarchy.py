# Academic People Hierarchy with super() and Validations
import re


class Person:
    total_persons = 0
    all_persons = []

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        Person.total_persons += 1
        Person.all_persons.append(self)

    @staticmethod
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.fullmatch(pattern, email):
            print("The entered email is valid.")
            return True
        else:
            print("The entered email is not valid.")
            return False

    @classmethod
    def from_string(cls, string):
        name, email, age = string.strip().split(",")
        if cls.is_valid_email(email):
            return cls(name, email, age)
        else:
            print("Oops! Email is not correct.")
            return None

    def __str__(self):
        return (f"Person's Details: \nPerson Name: {self.name} \n"
                f"Person Email: {self.email} \nPerson Age: {self.age}")

    @classmethod
    def display_all_persons(cls):
        if cls.all_persons:
            print("All Person's Details: ")
            print("--" * 30)
            for no, person in enumerate(cls.all_persons, start=1):
                print(f"Person {no}: ")
                print(person)
                print("--" * 30)
        else:
            print("There are no persons to show.")


class Staff(Person):
    total_staff = 0
    all_staff = []

    def __init__(self, name, email, age, emp_id, department):
        super().__init__(name, email, age)
        self.emp_id = emp_id
        self.department = department
        Staff.total_staff += 1
        Staff.all_staff.append(self)

    @staticmethod
    def is_valid_emp_id(emp_id):
        pattern = r'^[0-9]{6}$'
        if re.fullmatch(pattern, emp_id):
            print("The entered Employee ID is valid.")
            return True
        else:
            print("The entered Employee ID is not valid.")
            return False

    def __str__(self):
        return str(super().__str__() + (f"\nStaff Employee ID: {self.emp_id} \n"
                                        f"Staff Department: {self.department}")).replace("Person", "Staff")

    @classmethod
    def from_string(cls, string):
        name, email, age, emp_id, department = string.strip().split(",")
        if cls.is_valid_email(email):
            if cls.is_valid_emp_id(emp_id):
                return cls(name, email, age, emp_id, department)
            else:
                print("Oops! Employee ID is not correct.")
                return None
        else:
            print("Oops! Email is not correct.")
            return None

    @classmethod
    def display_all_staff(cls):
        if cls.all_staff:
            print("All Staff's Details: ")
            print("--" * 30)
            for no, staff in enumerate(cls.all_staff, start=1):
                print(f"Staff {no}: ")
                print(staff)
                print("--" * 30)
        else:
            print("There is no staff to show.")


class Faculty(Staff):
    total_faculty = 0
    all_faculty = []

    def __init__(self, name, email, age, emp_id, department, designation):
        super().__init__(name, email, int(age), emp_id, department)
        self.designation = designation
        self.courses_taught = []
        Faculty.total_faculty += 1
        Faculty.all_faculty.append(self)

    def add_course(self, course_name):
        if course_name not in self.courses_taught:
            self.courses_taught.append(course_name)
        else:
            print("The course is already added!")

    def __str__(self):
        return str(super().__str__() + (f"\nFaculty designation: {self.designation} \n"
                                        f"Courses taught by Faculty: "
                                        f"{self.courses_taught}")).replace("Staff", "Faculty")

    @classmethod
    def from_string(cls, string):
        name, email, age, emp_id, department, designation = string.strip().split(",")
        if cls.is_valid_email(email):
            if cls.is_valid_emp_id(emp_id):
                return cls(name, email, int(age), emp_id, department, designation)
            else:
                print("Oops! Employee ID is not correct.")
                return None
        else:
            print("Oops! Email is not correct.")
            return None

    @classmethod
    def display_all_faculty(cls):
        if cls.all_faculty:
            print("All Faculty's Details: ")
            print("--" * 30)
            for no, faculty in enumerate(cls.all_faculty, start=1):
                print(f"Faculty {no}: ")
                print(faculty)
                print("--" * 30)
        else:
            print("There is no faculty to show.")


if __name__ == "__main__":
    person1 = Person("Ali", "ali1@gmail.com", 21)
    person2 = Person.from_string("Hassan,hassan2@gmail.com,22")
    staff1 = Staff("Sohail", "sohail3@gmail.com", 23, "123456", "IT")
    staff2 = Staff.from_string("Abbas,abbas4@gmail.com,24,789012,HR")
    faculty1 = Faculty("Zaheer", "zaheer5@gmail.com", 25, "345678", "Accounting", "Associate Professor")
    faculty2 = Faculty.from_string("Asif,asif6@gmail.com,26,901234,Engineering,Assistant Professor")
    print(dir(faculty1))
    print(faculty2.__dict__)
    print(help(Faculty))
    print(Person.total_persons)
    Person.is_valid_email("alihassnianali98@gmail.com")
    Person.is_valid_email("alihassnianali98@gmail")
    print(Staff.total_staff)
    Staff.is_valid_emp_id("123456")
    Staff.is_valid_emp_id("12345")
    print(Faculty.total_faculty)
    faculty1.add_course("Physics")
    faculty2.add_course("Chemistry")
    faculty1.add_course("Mathematics")
    faculty2.add_course("Urdu")
    Person.display_all_persons()
    Staff.display_all_staff()
    Faculty.display_all_faculty()
    
