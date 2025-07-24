# Use Case: Accept student name, subject-wise marks, calculate grade.
# Exception Handling Goals:
# Raise error for negative marks
# Raise custom InvalidMarkError for marks > 100
# Catch and skip students with errors using loop-level exception
# Use try-except-else-finally block

import logging

# Configure logging
logging.basicConfig(filename='marksheet_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidMarkError(Exception):
    pass

def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def student_marksheet():
    students = []
    num_students = int(input("Enter number of students: "))
    
    for i in range(num_students):
        try:
            name = input(f"Enter name for student {i+1}: ")
            marks = []
            for subject in ['Math', 'Science', 'English']:
                mark = float(input(f"Enter {subject} marks for {name}: "))
                
                if mark < 0:
                    raise ValueError("Marks cannot be negative")
                if mark > 100:
                    raise InvalidMarkError("Marks cannot exceed 100")
                
                marks.append(mark)
                
        except ValueError as ve:
            logging.error(f"ValueError for student {name}: {str(ve)}")
            print(f"Error for {name}: {str(ve)}. Skipping student.")
            continue
        except InvalidMarkError as ime:
            logging.error(f"InvalidMarkError for student {name}: {str(ime)}")
            print(f"Error for {name}: {str(ime)}. Skipping student.")
            continue
        else:
            grade = calculate_grade(marks)
            students.append((name, marks, grade))
            print(f"{name}: Marks = {marks}, Grade = {grade}")
        finally:
            print(f"Processed student {i+1}")

    print("\nFinal Marksheet:")
    for name, marks, grade in students:
        print(f"Student: {name}, Marks: {marks}, Grade: {grade}")

if __name__ == "__main__":
    try:
        student_marksheet()
    except ValueError as ve:
        logging.error(f"Input error: {str(ve)}")
        print("Error: Invalid number of students entered")