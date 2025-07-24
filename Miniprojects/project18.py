# Use Case: Validate list of emails from input.
# Exception Handling Goals:
# Raise InvalidEmailFormatError
# Log all invalid emails
# Use try-except inside a list loop

import logging
import re

# Configure logging
logging.basicConfig(filename='email_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidEmailFormatError(Exception):
    pass

def validate_emails():
    emails = input("Enter emails (comma-separated): ").split(',')
    valid_emails = []
    
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    for email in emails:
        email = email.strip()
        try:
            if not email:
                raise InvalidEmailFormatError("Empty email address")
            if not re.match(email_pattern, email):
                raise InvalidEmailFormatError(f"Invalid email format: {email}")
            valid_emails.append(email)
        except InvalidEmailFormatError as iefe:
            logging.error(f"InvalidEmailFormatError: {str(iefe)}")
            print(f"Error: {str(iefe)}")
            
    print("\nValid Emails:")
    for email in valid_emails:
        print(email)
    return valid_emails

if __name__ == "__main__":
    validate_emails()