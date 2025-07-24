# Use Case: Allow user to attempt login max 3 times.
# Exception Handling Goals:
# Raise custom LoginFailedError after 3 failed attempts
# Catch and handle input errors
# Log exception with timestamp for each failed attempt

import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='login_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class LoginFailedError(Exception):
    pass

def login_system(username, password):
    correct_username = "admin"
    correct_password = "pass123"
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        try:
            user_input = input("Enter username: ")
            pass_input = input("Enter password: ")
            
            if user_input != correct_username or pass_input != correct_password:
                attempts += 1
                if attempts == max_attempts:
                    raise LoginFailedError("Maximum login attempts exceeded")
                logging.error(f"Failed login attempt {attempts} at {datetime.now()}")
                print(f"Invalid credentials. {max_attempts - attempts} attempts remaining.")
                continue
                
        except ValueError as ve:
            logging.error(f"Input error at {datetime.now()}: {str(ve)}")
            print("Error: Invalid input provided")
            attempts += 1
            continue
        else:
            print("Login successful!")
            return True
        finally:
            print("Login attempt processed")
            
    return False

if __name__ == "__main__":
    try:
        login_system("admin", "pass123")
    except LoginFailedError as lfe:
        logging.error(f"LoginFailedError: {str(lfe)}")
        print(f"Error: {str(lfe)}")