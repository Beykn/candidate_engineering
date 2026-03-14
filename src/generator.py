from faker import Faker
from src.models import Student

fake =  Faker('tr_TR')

def generate_students(num_students):
    student_list = []
    for i in range(num_students):
        student = Student(
            student_id= 200501110 + i ,
            student_name = fake.first_name(),
            student_surname = fake.last_name(),
            student_gpa = round(fake.random.uniform(2.0, 4.0), 2),
            student_class = fake.random.randint(1, 4)
        )
        student_list.append(student)
    return student_list