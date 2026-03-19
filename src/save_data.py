import pandas as pd 
import os 

def save_data(student_list):
    data = []
    for student in student_list:
        data.append({
                'student_id': student.student_id,
                'student_name': student.student_name,
                'student_surname': student.student_surname,
                'student_gpa': student.student_gpa,
                'student_class': student.student_class,
                'student_grade': student.student_grade
            
        })
        
    df = pd.DataFrame(data)
    filename = 'data/students_data.csv'
    
    if not os.path.exists('data'):
        os.makedirs('data')
        
    if not os.path.isfile(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)
    print(f"Data saved to {filename}")
    
def save_data_sortded_by_grade(student_list):
    data = []
    for student in student_list:
        data.append({
                'student_id': student.student_id,
                'student_name': student.student_name,
                'student_surname': student.student_surname,
                'student_gpa': student.student_gpa,
                'student_class': student.student_class,
                'student_grade': student.student_grade
            
        })
        
    df = pd.DataFrame(data)
    filename = 'data/students_data_sorted_by_grade.csv'
    
    if not os.path.exists('data'):
        os.makedirs('data')
        
    if not os.path.isfile(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)
    print(f"Data saved to {filename}")
    
    
        
def save_selected_students(student_list):
    data = []
    for student in student_list:
        data.append({
                'student_id': student.student_id,
                'student_name': student.student_name,
                'student_surname': student.student_surname,
                'student_gpa': student.student_gpa,
                'student_class': student.student_class,
                'student_grade': student.student_grade
            
        })
        
    df = pd.DataFrame(data)
    filename = 'data/selected_students.csv'
    
    if not os.path.exists('data'):
        os.makedirs('data')
        
    df.to_csv(filename, index=False)
    print(f"Selected students saved to {filename}")