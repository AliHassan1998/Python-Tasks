# Student Admission System
import re


class Student:
    total_students = 0
    all_students = []

    def __init__(self, name, roll_number, email, course):
        self.name = name
        self.roll_number = roll_number
        self.email = email
        self.course = course
        Student.all_students.append(self)
        Student.total_students += 1

    def __str__(self):
        return (f"Student Name: {self.name} \nStudent Roll Number: {self.roll_number} \n"
                f"Student Email: {self.email} \nStudent Course: {self.course}")

    @classmethod
    def from_string(cls, student_str):
        name, roll_number, email, course = student_str.split(",")
        pattern = r'^\d{6}$'
        if re.fullmatch(pattern, roll_number):
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            if re.fullmatch(pattern, email):
                return cls(name, roll_number, email, course)
            else:
                print("Error: Invalid Student's Email.")
                return None
        else:
            print("Error: Invalid Student's Roll Number.")
            return None

    @classmethod
    def display_all_students(cls):
        if cls.all_students:
            print("All Student's Details: ")
            print("--" * 30)
            for no, student in enumerate(cls.all_students, start=1):
                print(f"Student {no} Details: ")
                print(student)
                print("--" * 30)
        else:
            print("Oops! There are no students to show.")

    @classmethod
    def search_by_roll(cls, roll_number):
        for student in cls.all_students:
            if student.roll_number == roll_number:
                print("Requested Student's Details: ")
                print("--" * 30)
                print(student)
                print("--" * 30)
                break
        else:
            print(f"There is no student with the roll number: {roll_number}")

    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        if re.fullmatch(pattern, email):
            print(f"The email: {email} is valid.")
            return True
        else:
            print(f"Oops! The email: {email} is not valid.")
            return False


if __name__ == "__main__":
    student1 = Student("Ali", "123456", "ali1@gmail.com", "Physics")
    student2 = Student("Hassan", "789012", "hassan2@gmail.com", "Chemistry")
    student3 = Student.from_string("Sohail,345678,sohail3@gmail.com,Biology")
    student4 = Student.from_string("Abbas,90123,abbas4@gmail.com,Mathematics")
    student5 = Student.from_string("Zaheer,456789,zaheer5@gmail,English")
    Student.display_all_students()
    Student.search_by_roll("789012")
    Student.search_by_roll("78901")
    Student.is_valid_email("ali1@gmail.com")
    Student.is_valid_email("ali1@gmail")
    print(student1.__dict__)
    print(Student.__dict__)
    print(dir(Student))
    print(help(Student))
    print(Student.total_students)
