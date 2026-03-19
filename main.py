from src.generator import generate_students
from src.save_data import save_data, save_data_sortded_by_grade, save_selected_students
from src.search import selection_sort_by_grade

def start():
    num_students = input('Number of students to generate: ')

    try:
        num_students = int(num_students)
        num_students_to_select = int(input('Number of students to select: '))

        students = generate_students(num_students)
        save_data(students)

        selection_sort_by_grade(students)
        save_data_sortded_by_grade(students)

        selected_list = students[:num_students_to_select]
        save_selected_students(selected_list)

    except ValueError:
        print('Invalid input. Please enter a valid number.')
        return

if __name__ == "__main__":
    start()