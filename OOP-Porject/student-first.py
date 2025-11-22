class Subject:
    def __init__(self,name: str, grade: int) -> None:
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Subject name {self.name}, and your grade is: {self.grade}")

class Student:
    def __init__(self,name: str,student_id: str) -> None:
        self.name = name
        self.student_id = student_id
        self.subjects = []

    def add_grade(self,subject_name,grade_value):
        for subject in self.subjects:
            if subject.name == subject_name:
                subject.grade = grade_value
                print(f"updated grade for {subject_name} to {grade_value}")
        new_subject = Subject(subject_name,grade_value)
        self.subjects.append(new_subject)
        print(f"added new subject {subject_name} with a grade of {grade_value}")
    def get_gpa(self):
        if not self.subjects:
            return 0 
        total = sum(sub.grade for sub in self.subjects)
        return total / len(self.subjects)

    def display_grades(self):
        print("Grades for", self.name)
        for subject in self.subjects:
            print(f"{subject.name}: {subject.grade}")

class GradeBook:                                                                       
    def __init__(self) -> None:                                                        
        self.student = []

    def add_student(self,name,student_id):        
        self.student[student_id.name] = student_id                                     
        print(f"the student {student_id.name} has been added to the list.")            

    def find_student(self,student_id):                                                 
        if not student_id:                                                             
            print(f"there is no student in {self.student}")                            
        for student in self.student:                                                   
            if student.name == student_id:                                             
                print(f"this student {self.student} is on list")                       
            else:                                                                      
                print(f"this student {self.student} does appere on the list")          

    def record_grade(self,student_id,subject_name,grade_value):
        if not student_id:                                                             
            print(f"there is no student in {self.student}")                            
        for student in self.student:                                                   
            if student.name == student_id:                                             
                if subject_name == Subject:                                            
                    student.add_grade()                                                
                    return

    def display_all_students_gpa(self):
        if not self.student:
            print(f"there is no student in list  {self.student}")
        for student in self.student:
            student.get_gpa()

classes =   GradeBook()

#classes.add_student("mopo","12")
#classes.add_student("lassa","2")
#classes.add_student("lasd","6")

def main_menu(classes):
    while True:
        print("\n=== Animal Shelter Menu ===")
        print("1 - Admit a new student")
        print("2 - record grade")
        print("3 - view students Grades")
        print("4 - view GPA's")
        print("5 - Exit")
        
        choice = int(input("choose an option:"))
        if choice == "1":
            classes.add_student()
        elif choice == "2":
            classes.record_grade()
        elif choice == "3":
            classes.display_grades()
        elif choice == "4":
            classes.display_all_students_gpa()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("invalid input")

if __name__ == "__main__":
    classes = GradeBook()
    main_menu(classes)
