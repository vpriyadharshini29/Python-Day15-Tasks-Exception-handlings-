# Use Case: Accept income, credit score, and validate.
# Exception Handling Goals:
# Raise LowCreditScoreError
# Handle ValueError for non-numeric inputs
# Use try-else to display eligibility
# Use assert for positive income

import logging

# Configure logging
logging.basicConfig(filename='loan_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class LowCreditScoreError(Exception):
    pass

def check_loan_eligibility():
    try:
        income = float(input("Enter annual income: "))
        assert income > 0, "Income must be positive"
        
        credit_score = int(input("Enter credit score (300-850): "))
        if credit_score < 600:
            raise LowCreditScoreError("Credit score too low for loan eligibility")
            
    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        print("Error: Please enter valid numeric inputs")
        return False
    except AssertionError as ae:
        logging.error(f"AssertionError: {str(ae)}")
        print(f"Error: {str(ae)}")
        return False
    except LowCreditScoreError as lcse:
        logging.error(f"LowCreditScoreError: {str(lcse)}")
        print(f"Error: {str(lcse)}")
        return False
    else:
        if income >= 30000 and credit_score >= 600:
            print("Congratulations! You are eligible for a loan.")
            return True
        else:
            print("Sorry, you are not eligible for a loan.")
            return False

if __name__ == "__main__":
    check_loan_eligibility()