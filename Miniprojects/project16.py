# Use Case: Track and categorize expenses.
# Exception Handling Goals:
# Raise InvalidCategoryError
# Catch non-numeric expense entries
# Use try-except-finally to always show total

import logging

# Configure logging
logging.basicConfig(filename='expense_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidCategoryError(Exception):
    pass

def expense_tracker():
    categories = ['Food', 'Transport', 'Utilities', 'Entertainment']
    expenses = {cat: [] for cat in categories}
    total = 0.0
    
    while True:
        try:
            category = input("Enter category (Food/Transport/Utilities/Entertainment or 'done'): ")
            if category.lower() == 'done':
                break
                
            if category not in categories:
                raise InvalidCategoryError(f"Invalid category: {category}")
                
            amount = float(input(f"Enter expense amount for {category}: "))
            if amount < 0:
                raise ValueError("Expense amount cannot be negative")
                
            expenses[category].append(amount)
            total += amount
            
        except ValueError as ve:
            logging.error(f"ValueError: {str(ve)}")
            print(f"Error: Invalid amount - {str(ve)}")
        except InvalidCategoryError as ice:
            logging.error(f"InvalidCategoryError: {str(ice)}")
            print(f"Error: {str(ice)}")
        finally:
            print(f"Current total expenses: ${total:.2f}")
    
    print("\nExpense Summary:")
    for category, amounts in expenses.items():
        cat_total = sum(amounts)
        print(f"{category}: ${cat_total:.2f} ({len(amounts)} entries)")
    print(f"Total: ${total:.2f}")
    
    return expenses, total

if __name__ == "__main__":
    expense_tracker()