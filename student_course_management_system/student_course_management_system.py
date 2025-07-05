# Student Course Management System
import re


class Course:
    total_courses = 0
    all_courses = []

    def __init__(self, name, code, instructor):
        self.name = name
        self.instructor = instructor
        if Course.is_valid_code(code):
            self.code = code
            Course.total_courses += 1
            Course.all_courses.append(self)
        else:
            raise ValueError(f"The Entered Course Code is not valid: {code}.")

    @staticmethod
    def is_valid_code(code):
        pattern = r"^[A-Za-z]{3}\d{3}$"
        if re.fullmatch(pattern, code):
            return True
        else:
            return False

    def __str__(self):
        return (f"Course Details: \nCourse Name: {self.name} \n"
                f"Course Code: {self.code} \nCourse Instructor: {self.instructor}")

    def __repr__(self):
        return f"Course('{self.name}', '{self.code}', '{self.instructor}')"

    def __eq__(self, other):
        if isinstance(other, Course):
            return self.code == other.code
        return NotImplemented

    @classmethod
    def from_string(cls, string):
        name, code, instructor = string.strip().split(",")
        return cls(name, code, instructor)

    @classmethod
    def display_all_courses(cls):
        if cls.all_courses:
            print("All Courses Details: ")
            print("--" * 30)
            for no, course in enumerate(cls.all_courses, start=1):
                print(f"Course {no}: ")
                print(course)
                print("--" * 30)
        else:
            print("Oops! There are no courses to display.")


class Student:
    total_students = 0
    all_students = []

    def __init__(self, name, email, enrolled_courses=None):
        self.name = name
        if enrolled_courses is None:
            enrolled_courses = []
        self.enrolled_courses = enrolled_courses
        if Student.is_valid_email(email):
            self.email = email
            Student.total_students += 1
            Student.all_students.append(self)
        else:
            raise ValueError(f"The Entered Student Email is not valid: {email}.")

    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.fullmatch(pattern, email):
            return True
        else:
            return False

    def __str__(self):
        return (f"Student's Details: \nStudent Name: {self.name} \n"
                f"Student Email: {self.email} \nNumber of Courses Enrolled: {len(self.enrolled_courses)}")

    def __repr__(self):
        return f"Student('{self.name}', '{self.email}')"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.email == other.email
        return NotImplemented

    def __len__(self):
        return len(self.enrolled_courses)

    def __contains__(self, course):
        return course in self.enrolled_courses

    @classmethod
    def from_string(cls, string):
        name, email = string.strip().split(",")
        return cls(name, email)

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print("The course has been successfully enrolled!")
        else:
            print("You are already enrolled in this course.")

    @classmethod
    def display_all_students(cls):
        if cls.all_students:
            print("All Student's Details: ")
            print("--" * 30)
            for no, student in enumerate(cls.all_students, start=1):
                print(f"Student {no}: ")
                print(student)
                print("--" * 30)
        else:
            print("Oops! There are no Students to display.")

    def un_enroll(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            print("You have been successfully un_enrolled")
        else:
            print("You are not enrolled in the mentioned course.")


if __name__ == "__main__":
    course1 = Course.from_string("Math,ABC123,Mr. Bilal")
    course2 = Course.from_string("Physics,DEF456,Mrs. Beena")
    course3 = Course.from_string("Chemistry,GHI789,Mr. Asad")
    student1 = Student.from_string("Ali,ali1@gmail.com")
    student2 = Student.from_string("Hassan,hassan2@gmail.com")
    student1.enroll(course1)
    student1.enroll(course3)
    student2.enroll(course2)
    student2.enroll(course3)
    print(course1)
    print(repr(course1))
    print(course2)
    print(repr(course2))
    print(course3)
    print(repr(course3))
    print(student1)
    print(repr(student1))
    print(student2)
    print(repr(student2))
    print(course1 == course3)
    print(student1 == student2)
    print(len(student1))
    print(len(student2))
    print(course1 in student1)
    print(course1 in student2)
    Course.display_all_courses()
    Student.display_all_students()
    print(f"Total Courses are: {Course.total_courses}")
    print(f"Total Students are: {Student.total_students}")
    student1.un_enroll(course1)
