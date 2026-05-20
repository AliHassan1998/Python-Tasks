# Task: “Online Course System” using super() in Python
class Course:
    total_courses = 0
    all_courses = []

    def __init__(self, course_id, title, instructor, price):
        if Course.validate_course_id(course_id):
            self.course_id = course_id
        else:
            raise ValueError("Error: Oops! Course ID must be a non-empty string.")
        if Course.validate_title(title):
            self.title = title
        else:
            raise ValueError("Error: Oops! Course Title must be a non-empty string.")
        if Course.validate_instructor(instructor):
            self.instructor = instructor
        else:
            raise ValueError("Error: Oops! Course Instructor must be a non-empty string.")
        if Course.validate_price(price):
            self.price = float(price)
        else:
            raise ValueError("Error: Oops! Course Price must be a non-negative number.")
        Course.total_courses += 1
        Course.all_courses.append(self)

    @staticmethod
    def validate_course_id(course_id):
        if isinstance(course_id, str) and course_id.strip():
            return True
        else:
            return False

    @staticmethod
    def validate_title(title):
        if isinstance(title, str) and title.strip():
            return True
        else:
            return False

    @staticmethod
    def validate_instructor(instructor):
        if isinstance(instructor, str) and instructor.strip():
            return True
        else:
            return False

    @staticmethod
    def validate_price(price):
        if isinstance(price, (int, float)) and price >= 0:
            return True
        else:
            return False

    def course_details(self):
        return f"Course Details: \nID: {self.course_id} \nTitle: {self.title} \nInstructor: {self.instructor} \nPrice: {self.price}"

    def apply_discount(self, percent):
        if isinstance(percent, (int, float)) and 0 <= percent <= 100:
            discount = (percent / 100) * self.price
            self.price = self.price - discount
            return self.price
        else:
            raise ValueError("Error: Oops! Discount Percentage must be between 0 and 100 (numbers).")

    def is_free(self):
        if self.price == 0:
            return True
        else:
            return False

    def __str__(self):
        return f"Course's Details: \nCourse ID: {self.course_id} \nCourse Title: {self.title} \nCourse Instructor: {self.instructor} \nCourse Price: {self.price}"

    def __repr__(self):
        return f'Course("{self.course_id}", "{self.title}", "{self.instructor}", {self.price})'

    def __len__(self):
        return len(self.title)

    @classmethod
    def from_string(cls, string):
        course_id, title, instructor, price = string.strip().split(",")
        return cls(course_id, title, instructor, float(price))

    @classmethod
    def display_all_courses(cls):
        if cls.all_courses:
            print("All Course's Details: ")
            print("--" * 30)
            for no, course in enumerate(cls.all_courses, start=1):
                print(f"Course {no}: ")
                print(course)
                print("--" * 30)
        else:
            print("Oops! There are no courses to display.")


class PremiumCourse(Course):
    total_premium_courses = 0
    all_premium_courses = []

    def __init__(self, course_id, title, instructor, price, support_hours, certificate):
        super().__init__(course_id, title, instructor, price)
        if PremiumCourse.validate_support_hours(support_hours):
            self.support_hours = float(support_hours)
        else:
            raise ValueError("Error: Oops! Premium Course Support Hours must be a non-negative number.")
        if PremiumCourse.validate_certificate(certificate):
            self.certificate = certificate
        else:
            raise ValueError("Error: Oops! Premium Course Certificate must be a boolean value.")
        PremiumCourse.total_premium_courses += 1
        PremiumCourse.all_premium_courses.append(self)

    @staticmethod
    def validate_support_hours(support_hours):
        if isinstance(support_hours, (int, float)) and support_hours >= 0:
            return True
        else:
            return False

    @staticmethod
    def validate_certificate(certificate):
        if isinstance(certificate, bool):
            return True
        else:
            return False

    def course_details(self):
        return (super().course_details() + f" \nSupport Hours: {self.support_hours} \nCertificate Status: {self.certificate}").replace("Course", "Premium Course")

    def __str__(self):
        return (super().__str__() + f" \nCourse Support Hours: {self.support_hours} \nCourse Certificate Status: {self.certificate}").replace("Course", "Premium Course")

    def __repr__(self):
        return f'PremiumCourse("{self.course_id}", "{self.title}", "{self.instructor}", {self.price}, {self.support_hours}, {self.certificate})'

    def watch_support_session(self):
        return f"Watching Premium Support Session for Course: {self.title} with Course ID: {self.course_id} from Instructor: {self.instructor}"

    @classmethod
    def from_string(cls, string):
        course_id, title, instructor, price, support_hours, certificate = string.strip().split(",")
        return cls(course_id, title, instructor, float(price), float(support_hours), certificate.strip().lower() == "true")

    @classmethod
    def display_all_premium_courses(cls):
        if cls.all_premium_courses:
            print("All Premium Course's Details: ")
            print("--" * 30)
            for no, premium_course in enumerate(cls.all_premium_courses, start=1):
                print(f"Premium Course {no}: ")
                print(premium_course)
                print("--" * 30)
        else:
            print("Oops! There are no premium courses to display.")


if __name__ == "__main__":
    course1 = Course("C101", "Programming Fundamentals", "Ali", 1200)
    course2 = Course.from_string("C202,ICT,Hassan,1400")
    premium_course1 = PremiumCourse("P303", "Pre-Calculus", "Sohail", 1600, 12, True)
    premium_course2 = PremiumCourse.from_string("P404,English,Abbas,1800,13,False")
    print(course1)
    print(course2)
    print(premium_course1)
    print(premium_course2)
    print(repr(course1))
    print(repr(course2))
    print(repr(premium_course1))
    print(repr(premium_course2))
    print(course1.course_details())
    print(course2.course_details())
    print(premium_course1.course_details())
    print(premium_course2.course_details())
    print(course1.apply_discount(10))
    print(premium_course2.apply_discount(20))
    print(course2.is_free())
    print(premium_course1.is_free())
    print(len(course1))
    print(len(premium_course2))
    print(premium_course1.watch_support_session())
    print(premium_course2.watch_support_session())
    print(Course.total_courses)
    print(PremiumCourse.total_premium_courses)
    Course.display_all_courses()
    PremiumCourse.display_all_premium_courses()
