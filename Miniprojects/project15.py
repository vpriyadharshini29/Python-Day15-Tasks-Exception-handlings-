# Use Case: Accept attendance entries per student.
# Exception Handling Goals:
# Raise error if attendance > max days
# Catch invalid roll numbers
# Log absentees with exception info
# Use loop with try-except for multiple students

import logging

# Configure logging
logging.basicConfig(filename='attendance_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidAttendanceError(Exception):
    pass

def attendance_tracker():
    max_days = 30
    attendance_records = []
    
    num_students = int(input("Enter number of students: "))
    
    for i in range(num_students):
        try:
            roll_no = input(f"Enter roll number for student {i+1}: ")
            if not roll_no.isalnum():
                raise ValueError("Invalid roll number format")
                
            days_present = int(input(f"Enter attendance days for {roll_no}: "))
            if days_present > max_days:
                raise InvalidAttendanceError(f"Attendance cannot exceed {max_days} days")
            if days_present < 0:
                raise ValueError("Attendance cannot be negative")
                
            attendance_records.append((roll_no, days_present))
            
        except ValueError as ve:
            logging.error(f"ValueError for roll {roll_no}: {str(ve)}")
            print(f"Error: {str(ve)}. Skipping student.")
        except InvalidAttendanceError as iae:
            logging.error(f"InvalidAttendanceError for roll {roll_no}: {str(iae)}")
            print(f"Error: {str(iae)}. Skipping student.")
            
        if days_present < max_days * 0.75:  # Log absentees (less than 75% attendance)
            logging.warning(f"Low attendance for roll {roll_no}: {days_present}/{max_days} days")
    
    print("\nAttendance Records:")
    for roll_no, days in attendance_records:
        print(f"Roll {roll_no}: {days}/{max_days} days")

if __name__ == "__main__":
    try:
        attendance_tracker()
    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        print("Error: Invalid number of students entered")