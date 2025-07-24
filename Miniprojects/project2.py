# Use Case: Collect name, email, age, and password.
# Exception Handling Goals:
# Raise ValueError if age is not integer or < 13
# Raise TypeError if name/email is not string
# Raise custom PasswordTooWeakError
# Catch all and log invalid fields
# Use assert for pre-checks

import logging
import re

# Configure logging
logging.basicConfig(filename='registration_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class PasswordTooWeakError(Exception):
    pass

def validate_registration(name, email, age, password):
    try:
        # Pre-checks with assert
        assert isinstance(name, str), "Name must be a string"
        assert isinstance(email, str), "Email must be a string"
        assert len(name.strip()) > 0, "Name cannot be empty"
        assert len(email.strip()) > 0, "Email cannot be empty"
        
        # Validate age
        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        if age < 13:
            raise ValueError("Age must be at least 13")
            
        # Validate email format
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")
            
        # Validate password strength
        if len(password) < 8 or not any(c.isdigit() for c in password) or not any(c.isupper() for c in password):
            raise PasswordTooWeakError("Password must be at least 8 characters long, with digits and uppercase letters")
            
    except (TypeError, ValueError, PasswordTooWeakError, AssertionError) as e:
        logging.error(f"Registration error: {str(e)}")
        print(f"Error: {str(e)}")
        return False
    else:
        print("Registration successful")
        return True
    finally:
        print("Registration validation completed")

if __name__ == "__main__":
    try:
        name = input("Enter name: ")
        email = input("Enter email: ")
        age = int(input("Enter age: "))
        password = input("Enter password: ")
        validate_registration(name, email, age, password)
    except ValueError as ve:
        logging.error(f"Input error: {str(ve)}")
        print("Error: Invalid input provided")