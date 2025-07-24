# Use Case: Simulate withdrawal, deposit, balance check.
# Exception Handling Goals:
# Raise InsufficientFundsError if withdrawal > balance
# Catch non-numeric input
# Use nested try for each transaction
# Use assert to validate positive amounts

import logging

# Configure logging
logging.basicConfig(filename='atm_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InsufficientFundsError(Exception):
    pass

def atm_simulator():
    balance = 1000.0
    
    while True:
        print("\n1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == '4':
            break
            
        try:
            if choice not in ['1', '2', '3']:
                raise ValueError("Invalid option")
                
            if choice == '3':
                print(f"Current balance: ${balance:.2f}")
                continue
                
            try:
                amount = float(input("Enter amount: "))
                assert amount > 0, "Amount must be positive"
                
                if choice == '1':
                    if amount > balance:
                        raise InsufficientFundsError("Insufficient funds")
                    balance -= amount
                    print(f"Withdrawn ${amount:.2f}. New balance: ${balance:.2f}")
                elif choice == '2':
                    balance += amount
                    print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
                    
            except AssertionError as ae:
                logging.error(f"AssertionError: {str(ae)}")
                print(f"Error: {str(ae)}")
            except InsufficientFundsError as ife:
                logging.error(f"InsufficientFundsError: {str(ife)}")
                print(f"Error: {str(ife)}")
                
        except ValueError as ve:
            logging.error(f"ValueError: {str(ve)}")
            print(f"Error: Invalid input - {str(ve)}")
            
if __name__ == "__main__":
    atm_simulator()