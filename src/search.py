from src.save_data import save_data_sortded_by_grade
def selection_sort_by_grade(student_list):
    n = len(student_list)

    for i in range(n):
        max_index = i

        for j in range(i + 1, n):
            if student_list[j].student_grade > student_list[max_index].student_grade:
                max_index = j

        # swap
        student_list[i], student_list[max_index] = student_list[max_index], student_list[i]

    return student_list

 