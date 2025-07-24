# Use Case: Generate strong password from user specs.
# Exception Handling Goals:
# Raise WeakPasswordCriteriaError if specs weak
# Handle user input issues
# Use assert for length validation
# try-else-finally to wrap generation

import logging
import random
import string

# Configure logging
logging.basicConfig(filename='password_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class WeakPasswordCriteriaError(Exception):
    pass

def generate_password(length, use_upper, use_digits, use_special):
    try:
        assert length >= 8, "Password length must be at least 8 characters"
        
        if not (use_upper or use_digits or use_special):
            raise WeakPasswordCriteriaError("At least one character type (uppercase, digits, special) must be selected")
            
        chars = string.ascii_lowercase
        if use_upper:
            chars += string.ascii_uppercase
        if use_digits:
            chars += string.digits
        if use_special:
            chars += string.punctuation
            
        password = ''.join(random.choice(chars) for _ in range(length))
        
        # Verify password meets criteria
        if use_upper and not any(c.isupper() for c in password):
            raise WeakPasswordCriteriaError("Generated password lacks uppercase letters")
        if use_digits and not any(c.isdigit() for c in password):
            raise WeakPasswordCriteriaError("Generated password lacks digits")
        if use_special and not any(c in string.punctuation for c in password):
            raise WeakPasswordCriteriaError("Generated password lacks special characters")
            
        return password
        
    except AssertionError as ae:
        logging.error(f"AssertionError: {str(ae)}")
        print(f"Error: {str(ae)}")
        return None
    except WeakPasswordCriteriaError as wpce:
        logging.error(f"WeakPasswordCriteriaError: {str(wpce)}")
        print(f"Error: {str(wpce)}")
        return None
    else:
        print(f"Generated password: {password}")
        return password
    finally:
        print("Password generation attempt completed")

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
        
        generate_password(length, use_upper, use_digits, use_special)
    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        print("Error: Invalid input provided")