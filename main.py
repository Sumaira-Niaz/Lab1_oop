class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def passed(self):
        return self.marks >= 50

    def __str__(self):
        return f"{self.name} ({self.marks}): {'Pass' if self.passed() else 'Fail'}"

s1 = Student("Ali", 72)
s2 = Student("Sara", 45)
s3 = Student("Omar", 50)

students = [s1, s2, s3]

for student in students:
    print(student)
    from course import Course

    course = Course("OOP")

    course.add_student("Ali", 72)
    course.add_student("Sara", 85)
    course.add_student("Omar", 50)

    print(len(course))
    print(course.average())
    print(course.top_student())

    from course import load_course

    course = load_course("marks.txt","OOP" )

    print(f"Total Students: {len(course)}")
    print(f"Average Marks: {course.average():.2f}")
    print(f"Top Student: {course.top_student()}")
    