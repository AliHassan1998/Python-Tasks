# Object Introspection Explorer
import re


class Course:
    """
    This class contain all the details of Courses
    """
    total_courses = 0
    all_courses = []

    def __init__(self, course_name, course_code, credits):
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits
        Course.all_courses.append(self)
        Course.total_courses += 1

    def __str__(self):
        return (f"Course's Details: \nCourse Name: {self.course_name} \n"
                f"Course Code: {self.course_code} \nCourse Credits: {self.credits}")

    @classmethod
    def get_courses_summary(cls):
        print("All Course's Details: ")
        print("--" * 30)
        if cls.all_courses:
            for no, course in enumerate(cls.all_courses, start=1):
                print(f"Course {no}: ")
                print(course)
                print("--" * 30)
        else:
            print("Oops! There are no courses to show.")

    @classmethod
    def from_string(cls, string):
        course_name, course_code, credits = string.strip().split(",")
        return cls(course_name, course_code, int(credits))


class Instructor:
    """
        This class contain all the details of Instructors
        """
    def __init__(self, name, email, department):
        self.name = name
        self.email = email
        self.department = department

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
    def from_string(cls, string):
        name, email, department = string.strip().split(",")
        if cls.is_valid_email(email):
            return cls(name, email, department)
        else:
            print("Error: Please enter correct Instructor's details.")


if __name__ == "__main__":
    course1 = Course("Physics", "123", "3")
    course2 = Course.from_string("Chemistry,456,4")
    course3 = Course.from_string("Biology,789,3")
    instructor1 = Instructor("Ali", "ali1@gmail.com", "Computer Science")
    instructor2 = Instructor.from_string("Hassan,hassan2@gmail.com,Mathematics")
    instructor3 = Instructor.from_string("Sohail,sohail3gmail,History")
    print(course1.__dict__)
    print(instructor2.__dict__)
    print(Course.__dict__)
    print(Instructor.__dict__)
    print(dir(course2))
    print(dir(instructor1))
    print(help(Course))
    print(help(Instructor))
    Course.get_courses_summary()
