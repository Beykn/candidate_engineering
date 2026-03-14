from dataclasses import dataclass

@dataclass
class Student:
    student_id: int
    student_name: str
    student_surname: str
    student_gpa: float
    student_class: int
    
    student_grade: float = 0.0
    
    def calculate_grade(self):
        self.puan = round((self.student_gpa / 4.0) * 100, 2)