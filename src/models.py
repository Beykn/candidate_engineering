from dataclasses import dataclass

@dataclass
class Student:
    student_id: int
    student_name: str
    student_surname: str
    student_gpa: float
    student_class: int
    
    student_grade: float = 0.0
    
    def __post_init__(self):
        self.calculate_grade()

    def calculate_grade(self):
        self.student_grade = round((self.student_gpa / 4.0) * 100, 2)
        
# TODO: add company model and generate company data for internship matching