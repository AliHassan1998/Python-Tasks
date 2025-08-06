# "University System" using Single Inheritance
class Person:
    total_persons = 0
    all_persons = []

    def __init__(self, name, age):
        if Person.validate_name(name):
            self.name = name
        else:
            raise TypeError("Error: Oops! Person Name must be non-empty string.")
        if Person.validate_age(age):
            self.age = age
        else:
            raise ValueError("Error: Oops! Person Age must be a greater or equal to 16 integer value.")
        self.email = f"{name.lower().replace(' ', '_')}@university.com"
        Person.total_persons += 1
        Person.all_persons.append(self)

    @staticmethod
    def validate_name(name):
        if name and isinstance(name, str):
            return True
        else:
            return False

    @staticmethod
    def validate_age(age):
        if age >= 16 and isinstance(age, int):
            return True
        else:
            return False

    def __str__(self):
        return f"Person's Details: \nPerson's Name: {self.name} \nPerson's Age: {self.age} \n" \
               f"Person's Email: {self.email}"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name.lower() == other.name.lower() and self.age == other.age
        return NotImplemented

    def __len__(self):
        return len(self.name.replace(" ", ""))

    @classmethod
    def from_string(cls, string):
        try:
            name, age = string.strip().split(",")
            return cls(name, int(age))
        except Exception as e:
            print(f"Oops! An error occurred: {e}")

    @classmethod
    def display_all_persons(cls):
        if cls.all_persons:
            print("All Person's Details: ")
            print("--" * 30)
            for no, person in enumerate(cls.all_persons, start=1):
                print(f"Person: {no}: ")
                print(person)
                print("--" * 30)
        else:
            print("Oops! There are no Persons to display.")


class Student(Person):
    total_students = 0
    all_students = []

    def __init__(self, name, age, student_id, gpa, courses=None):
        super().__init__(name, age)
        if Student.validate_student_id(student_id):
            self.student_id = student_id
        else:
            raise TypeError("Oops! Student ID must be a non-empty string.")
        if Student.validate_gpa(gpa):
            self.gpa = gpa
        else:
            raise ValueError("Oops! Student GPA must be between 0.0 and 4.0 float value.")
        if courses is None:
            self.courses = []
        else:
            self.courses = courses
        Student.total_students += 1
        Student.all_students.append(self)

    @staticmethod
    def validate_student_id(student_id):
        if student_id and isinstance(student_id, str):
            return True
        else:
            return False

    @staticmethod
    def validate_gpa(gpa):
        if 0.0 <= gpa <= 4.0 and isinstance(gpa, float):
            return True
        else:
            return False

    def __str__(self):
        return str(super().__str__() + f"\nStudent's ID: {self.student_id} \nStudent's GPA: {self.gpa} \n"
                                       f"Student's Enrolled Courses: {self.courses}").replace("Person", "Student")

    def __repr__(self):
        return f"Student('{self.name}', {self.age}, '{self.student_id}', {self.gpa})"

    def __len__(self):
        return len(self.courses)

    def __call__(self, course):
        if course not in self.courses:
            if len(self.courses) <= 6:
                self.courses.append(course)
                return self.courses
            else:
                return f"Oops! You can't Enroll more than 6 courses."
        else:
            return f"Oops! The course is already enrolled."

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name.lower() == other.name.lower() and self.age == other.age and self.gpa == other.gpa
        return NotImplemented

    @classmethod
    def from_string(cls, string):
        try:
            name, age, student_id, gpa = string.strip().split(",")
            return cls(name, int(age), student_id, float(gpa))
        except Exception as e:
            print(f"Oops! An error occurred: {e}")

    def display_courses(self):
        if self.courses:
            print(f"All Courses Enrolled by {self.name}: ")
            print("--" * 30)
            for no, course in enumerate(self.courses, start=1):
                print(f"{no}: {course}")
                print("--" * 30)
        else:
            print("Oops! There are no courses to display.")

    def remove_course(self, course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)
            return self.courses
        else:
            return f"Oops! You are not enrolled in this course: {course_name}"

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


if __name__ == "__main__":
    person1 = Person("Ali", 16)
    person2 = Person.from_string("Hassan, 18")
    student1 = Student("Sohail", 20, "EME101", 3.2)
    student2 = Student.from_string("Abbas,22,RNR102,3.4")
    print(student1 == student2)
    student1("Physics")
    student2("Chemistry")
    student1("Biology")
    student2("Mathematics")
    student1.display_courses()
    student2.display_courses()
    print(person1)
    print(repr(person1))
    print(person2)
    print(repr(person2))
    print(student1)
    print(repr(student1))
    print(student2)
    print(repr(student2))
    print(person1 == person2)
    print(len(person1))
    print(len(person2))
    print(len(student1))
    print(len(student2))
    print(f"Total Persons are {Person.total_persons} out of which {Student.total_students} are Students.")
    Person.display_all_persons()
    Student.display_all_students()
    student1.remove_course("Biology")
    student1.display_courses()
