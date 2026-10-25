"""Lab 1 starter: complete every TODO."""


class Course:
    """A course that stores students and their marks."""

    def __init__(self, name):
        self.name = name
        self.marks = {}            # student name -> marks
    def add_student(self, student, marks):
        if not 0 <= marks <= 100:
            raise ValueError("Invalid marks")
        self.marks[student] = marks
    def average(self):
        return sum(self.marks.values()) / len(self.marks)
    def top_student(self):
        return max(self.marks, key=self.marks.get)
    def __len__(self):
        return len(self.marks)
    def __str__(self):
        return f"{self.name}: {len(self.marks)} students, average {self.average():.1f}"
    def remove_student(self, name: str) -> None:
        """Remove a student, or raise KeyError if missing."""
        if name not in self.marks:
            raise KeyError(f"No student named {name}")
        del self.marks[name]
def load_course(filename, course_name):
    course = Course(course_name)
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 2:
                student, marks_str = parts[0].strip(), parts[1].strip()
                try:
                    marks = int(marks_str)
                    course.add_student(student, marks)
                except ValueError:
                    pass
    return course
if __name__ == "__main__":
    test = Course("Test")
    test.add_student("A", 50)
    print(test)
    