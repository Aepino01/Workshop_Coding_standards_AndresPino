class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = "?"

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0

        total = sum(self.grades)
        return total / len(self.grades)

    def check_honor(self):
        if self.calculate_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        if 0 <= index < len(self.grades):
            del self.grades[index]

    def report(self):
        print(f"ID: {self.id}")
        print(f"Name is: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Final Grade = {self.calculate_average():.2f}")


def start_run():
    student = Student("x", "")
    student.add_grade(100)
    student.add_grade(50)
    student.calculate_average()
    student.check_honor()
    student.delete_grade(1)
    student.report()


start_run()