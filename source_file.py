"""Student grade management system."""

class Student:
    """Represent a student and manage their grades."""

    def __init__(self, student_id, name):
        """Initialize a student with an ID and name."""
        if not student_id or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")

        if not name or not name.strip():
            raise ValueError("Student name cannot be empty.")

        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.letter_grade = "N/A"

    def add_grade(self, grade):
        """Add a valid grade between 0 and 100."""
        try:
            grade = float(grade)
        except (TypeError, ValueError):
            print("Error: Grade must be a number.")
            return

        if not 0 <= grade <= 100:
            print("Error: Grade must be between 0 and 100.")
            return

        self.grades.append(grade)

    def calculate_average(self):
        """Calculate and return the average of all grades."""
        if not self.grades:
            return 0.0

        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self):
        """Determine and return the letter grade based on the average."""
        average = self.calculate_average()

        if average >= 90:
            self.letter_grade = "A"
        elif average >= 80:
            self.letter_grade = "B"
        elif average >= 70:
            self.letter_grade = "C"
        elif average >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

        return self.letter_grade

    def determine_pass_fail(self):
        """Determine and return whether the student passed or failed."""
        average = self.calculate_average()
        self.is_passed = average >= 60

        return "Passed" if self.is_passed else "Failed"

    def report(self):
        """Display the student's grades, average, letter grade, and status."""
        average = self.calculate_average()
        letter_grade = self.determine_letter_grade()
        result = self.determine_pass_fail()

        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"Status: {result}")


def start_run():
    """Create a student, add grades, and display the report."""
    try:
        student = Student("001", "Andres")

        student.add_grade(95.0)
        student.add_grade(72.5)
        student.add_grade(88.0)

        student.report()

        print("\nTesting invalid grades:")
        student.add_grade("Fifty")
        student.add_grade(150)

    except ValueError as error:
        print(f"Error: {error}")


start_run()
