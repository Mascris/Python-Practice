class Subject:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"{self.name}: {self.grade}")

class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.subjects = []    

    def add_grade(self, subject_name, grade_value):
        for subject in self.subjects:
            if subject.name == subject_name:
                subject.grade = grade_value
                print(f"Updated grade for {subject_name} to {grade_value}")
                return

        new_subject = Subject(subject_name, grade_value)
        self.subjects.append(new_subject)
        print(f"Added {subject_name} with grade {grade_value}")

    def get_gpa(self):
        if not self.subjects:
            return 0
        total = sum(sub.grade for sub in self.subjects)
        return total / len(self.subjects)

    def display_grades(self):
        print(f"\nGrades for {self.name}:")
        for subject in self.subjects:
            subject.display_info()

class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, name, student_id):
        if student_id in self.students:
            print("Student already exists!")
            return

        student = Student(name, student_id)
        self.students[student_id] = student
        print(f"Student {name} added.")

    def find_student(self, student_id):
        return self.students.get(student_id, None)

    def record_grade(self, student_id, subject_name, grade_value):
        student = self.find_student(student_id)
        if not student:
            print("Student not found.")
            return
        student.add_grade(subject_name, grade_value)

    def display_all_students_gpa(self):
        for student in self.students.values():
            print(f"{student.name}: GPA = {student.get_gpa()}")


def main_menu(classes):
    while True:
        print("\n=== GradeBook Menu ===")
        print("1 - Add a new student")
        print("2 - Record a grade")
        print("3 - View student grades")
        print("4 - View all GPAs")
        print("5 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Student name: ")
            sid = input("Student ID: ")
            classes.add_student(name, sid)

        elif choice == "2":
            sid = input("Student ID: ")
            subject = input("Subject name: ")
            grade = int(input("Grade: "))
            classes.record_grade(sid, subject, grade)

        elif choice == "3":
            sid = input("Student ID: ")
            student = classes.find_student(sid)
            if student:
                student.display_grades()
            else:
                print("Student not found.")

        elif choice == "4":
            classes.display_all_students_gpa()

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid input.")

if __name__ == "__main__":
    classes = GradeBook()
    main_menu(classes)
