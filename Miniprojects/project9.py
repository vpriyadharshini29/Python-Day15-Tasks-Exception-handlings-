# Use Case: Accept grades from user, retry until valid.
# Exception Handling Goals:
# Use recursion inside try block
# Catch ValueError and retry
# Use finally to print final count of valid entries

import logging

# Configure logging
logging.basicConfig(filename='grade_calculator_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_grade_recursive(grades=None, count=0):
    if grades is None:
        grades = []
        
    try:
        grade = float(input("Enter a grade (or -1 to finish): "))
        if grade == -1:
            return grades, count
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        grades.append(grade)
        count += 1
        return get_grade_recursive(grades, count)
        
    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        print(f"Error: Invalid grade - {str(ve)}. Try again.")
        return get_grade_recursive(grades, count)
    finally:
        print(f"Processed {count} valid grades so far")
        
if __name__ == "__main__":
    grades, valid_count = get_grade_recursive()
    print("\nFinal Grades:")
    for i, grade in enumerate(grades, 1):
        print(f"Grade {i}: {grade}")
    print(f"Total valid grades entered: {valid_count}")