from online_course_system.online_course_system import Course, PremiumCourse

course = Course("C101", "Python", "Ali", 1000)

premium = PremiumCourse(
    "P202",
    "Deep Learning",
    "Hassan",
    2000,
    10,
    True
)

assert len(course) == len("Python")

assert premium.is_free() is False

assert "Deep Learning" in premium.watch_support_session()
