# Use Case: Perform basic math operations (+, -, *, /, %).
# Exception Handling Goals:
# Handle ZeroDivisionError
# Handle ValueError for non-numeric inputs
# Use try-else-finally for flow control
# Raise custom InvalidOperationError if operator is invalid
# Log all exceptions to a file

import logging

# Configure logging
logging.basicConfig(filename='calculator_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidOperationError(Exception):
    pass

def smart_calculator():
    print("Enter two numbers and an operator (+, -, *, /, %)")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator: ")
        
        if operator not in ['+', '-', '*', '/', '%']:
            raise InvalidOperationError("Invalid operator. Use +, -, *, /, or %")
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '%':
            result = num1 % num2
            
    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        print("Error: Please enter valid numeric inputs")
        return None
    except ZeroDivisionError:
        logging.error("ZeroDivisionError: Division or modulo by zero")
        print("Error: Cannot divide or modulo by zero")
        return None
    except InvalidOperationError as ioe:
        logging.error(f"InvalidOperationError: {str(ioe)}")
        print(f"Error: {str(ioe)}")
        return None
    else:
        print(f"Result: {result}")
        return result
    finally:
        print("Calculation attempt completed")

if __name__ == "__main__":
    smart_calculator()