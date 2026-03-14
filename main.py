from src.generator import generate_students
from src.save_data import save_data

def start():
    num_students = input('Number of students to generate: ')
    try:
        num_students = int(num_students)
        students = generate_students(num_students)
        save_data(students)
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        return
    
if __name__ == "__main__":
    start()