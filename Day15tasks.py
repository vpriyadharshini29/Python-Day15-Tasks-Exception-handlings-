import logging
import re
import os

# Configure logging
logging.basicConfig(
    filename='exceptions.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Custom Exceptions
class NegativeNumberError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class GradeOutOfRangeError(Exception):
    pass

class UnauthorizedAccessError(Exception):
    pass

class InvalidFileFormatError(Exception):
    pass

class LoginAttemptsExceededError(Exception):
    pass

class FileTooLargeError(Exception):
    pass

class InvalidTemperatureError(Exception):
    pass

# Basic Exception Handling (1–10)
def task_1_divide_numbers():
    """Divide two numbers, handle ZeroDivisionError and ValueError."""
    try:
        a, b = float(input("Enter first number: ")), float(input("Enter second number: "))
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except ValueError:
        print("Error: Please enter valid numbers!")
    else:
        print(f"Result: {result}")

def task_2_validate_age():
    """Validate age input, raise error if non-numeric or negative."""
    try:
        age = int(input("Enter age: "))
        if age < 0:
            raise NegativeNumberError("Age cannot be negative!")
    except ValueError:
        print("Error: Age must be a number!")
    except NegativeNumberError as e:
        print(f"Error: {e}")

def task_3_open_file():
    """Open a file, handle FileNotFoundError."""
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File not found!")

def task_4_read_closed_file():
    """Attempt to read from a closed file, handle ValueError."""
    try:
        f = open("test.txt", 'r')
        f.close()
        f.read()  # Attempt to read closed file
    except ValueError:
        print("Error: Cannot read from a closed file!")
    except FileNotFoundError:
        print("Error: File not found!")

def task_5_list_index():
    """Handle IndexError when accessing list by user input."""
    lst = [1, 2, 3]
    try:
        index = int(input("Enter index (0-2): "))
        print(lst[index])
    except IndexError:
        print("Error: Index out of range!")
    except ValueError:
        print("Error: Index must be a number!")

def task_6_dict_key():
    """Handle KeyError for missing dictionary key."""
    d = {'a': 1, 'b': 2}
    try:
        key = input("Enter key: ")
        print(d[key])
    except KeyError:
        print("Error: Key not found!")

def task_7_convert_number():
    """Convert user input to int, catch ValueError."""
    try:
        num = int(input("Enter a number: "))
        print(f"Number: {num}")
    except ValueError:
        print("Error: Invalid number!")

def task_8_type_error():
    """Catch TypeError when adding string and integer."""
    try:
        result = "text" + 5
    except TypeError:
        print("Error: Cannot add string and integer!")

def task_9_attribute_error():
    """Catch AttributeError for non-existent method."""
    try:
        obj = "string"
        obj.non_existent_method()
    except AttributeError:
        print("Error: Method does not exist!")

def task_10_name_error():
    """Handle NameError for undefined variable."""
    try:
        print(undefined_variable)
    except NameError:
        print("Error: Variable not defined!")

# Multiple Except, Else, Finally Blocks (11–20)
def task_11_try_else():
    """Divide numbers with try-else."""
    try:
        a, b = float(input("Enter first number: ")), float(input("Enter second number: "))
        result = a / b
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
    else:
        print(f"Result: {result}")

def task_12_try_finally():
    """Use finally to print 'Done'."""
    try:
        a, b = float(input("Enter first number: ")), float(input("Enter second number: "))
        result = a / b
    except ValueError:
        print("Error: Invalid number!")
    finally:
        print("Done")

def task_13_multiple_except():
    """Multiple except blocks for ValueError and ZeroDivisionError."""
    try:
        a, b = float(input("Enter first number: ")), float(input("Enter second number: "))
        result = a / b
    except ValueError:
        print("Error: Invalid number!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print(f"Result: {result}")

def task_14_finally_uncaught():
    """Finally runs even with uncaught exception."""
    try:
        a = int(input("Enter number: "))
        result = 10 / (a - 5)  # May raise ZeroDivisionError or ValueError
    except ValueError:
        print("Error: Invalid number!")
    finally:
        print("Finally block executed")

def task_15_else_finally():
    """Combine else and finally."""
    try:
        a, b = float(input("Enter first number: ")), float(input("Enter second number: "))
        result = a / b
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
    else:
        print(f"Result: {result}")
    finally:
        print("Operation completed")

def task_16_file_finally():
    """Handle file reading with finally to close file."""
    f = None
    try:
        filename = input("Enter filename: ")
        f = open(filename, 'r')
        print(f.read())
    except FileNotFoundError:
        print("Error: File not found!")
    finally:
        if f:
            f.close()
            print("File closed")

def task_17_nested_try():
    """Nested try-except blocks."""
    try:
        a = float(input("Enter number: "))
        try:
            result = 10 / a
        except ZeroDivisionError:
            print("Inner: Division by zero!")
    except ValueError:
        print("Outer: Invalid number!")
    else:
        print(f"Result: {result}")

def task_18_multiple_exceptions():
    """Handle multiple exception types."""
    try:
        a = float(input("Enter number: "))
        lst = [1, 2]
        print(lst[int(a)] / a)
    except ValueError:
        print("Error: Invalid number!")
    except IndexError:
        print("Error: Index out of range!")
    except ZeroDivisionError:
        print("Error: Division by zero!")

def task_19_generic_exception():
    """Use Exception as fallback."""
    try:
        a = float(input("Enter number: "))
        print(10 / a)
    except ValueError:
        print("Error: Invalid number!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.error(f"Unexpected error: {e}")

def task_20_correct_nesting():
    """Correctly nested try-except-finally."""
    try:
        try:
            a = float(input("Enter number: "))
            result = 10 / a
        except ValueError:
            print("Inner: Invalid number!")
            raise
    except Exception as e:
        print(f"Outer: Caught {e}")
    finally:
        print("Finally block")

# Raise Statement (21–30)
def task_21_raise_negative():
    """Raise ValueError for negative number."""
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise ValueError("Number cannot be negative!")
        print(f"Number: {num}")
    except ValueError as e:
        print(f"Error: {e}")

def task_22_raise_type():
    """Raise TypeError if argument not string."""
    def check_string(arg):
        if not isinstance(arg, str):
            raise TypeError("Argument must be a string!")
        return arg
    try:
        print(check_string(123))
    except TypeError as e:
        print(f"Error: {e}")

def task_23_positive_integer():
    """Function accepts only positive integers."""
    def only_positive(num):
        if not isinstance(num, int) or num <= 0:
            raise ValueError("Only positive integers allowed!")
        return num
    try:
        num = int(input("Enter positive integer: "))
        print(only_positive(num))
    except ValueError as e:
        print(f"Error: {e}")

def task_24_login_system():
    """Simulate login, raise error for wrong password."""
    correct_password = "pass123"
    try:
        password = input("Enter password: ")
        if password != correct_password:
            raise ValueError("Incorrect password!")
        print("Login successful")
    except ValueError as e:
        print(f"Error: {e}")

def task_25_missing_key():
    """Raise error for missing dictionary key."""
    d = {'name': 'Alice'}
    try:
        key = input("Enter key: ")
        if key not in d:
            raise KeyError(f"Key '{key}' not found!")
        print(d[key])
    except KeyError as e:
        print(f"Error: {e}")

def task_26_custom_zero_division():
    """Raise ZeroDivisionError with custom message."""
    try:
        a, b = float(input("Enter first number: ")), float(input("Enter second number: "))
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero, please provide non-zero denominator!")
        print(a / b)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid number!")

def task_27_assert_even():
    """Use assert to raise error if number not even."""
    try:
        num = int(input("Enter an even number: "))
        assert num % 2 == 0, "Number must be even!"
        print(f"Even number: {num}")
    except AssertionError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid number!")

def task_28_validate_email():
    """Validate email format, raise ValueError if invalid."""
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError("Invalid email format!")
        return email
    try:
        email = input("Enter email: ")
        print(is_valid_email(email))
    except ValueError as e:
        print(f"Error: {e}")

def task_29_empty_list():
    """Raise error if list is empty."""
    lst = []
    try:
        if not lst:
            raise ValueError("List is empty!")
        print(lst[0])
    except ValueError as e:
        print(f"Error: {e}")

def task_30_empty_file():
    """Raise error if file is empty."""
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as f:
            content = f.read()
            if not content:
                raise ValueError("File is empty!")
            print(content)
    except FileNotFoundError:
        print("Error: File not found!")
    except ValueError as e:
        print(f"Error: {e}")

# Custom/User-Defined Exceptions (31–40)
def task_31_negative_number_error():
    """Raise custom NegativeNumberError."""
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise NegativeNumberError("Negative numbers not allowed!")
        print(f"Number: {num}")
    except NegativeNumberError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid number!")

def task_32_invalid_age():
    """Use InvalidAgeError for age validation."""
    try:
        age = int(input("Enter age: "))
        if age < 0 or age > 120:
            raise InvalidAgeError("Age must be between 0 and 120!")
        print(f"Age: {age}")
    except InvalidAgeError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid number!")

def task_33_banking_app():
    """Banking app with InsufficientFundsError."""
    balance = 1000
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            raise InsufficientFundsError("Insufficient funds!")
        balance -= amount
        print(f"New balance: {balance}")
    except InsufficientFundsError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid amount!")

def task_34_grading_app():
    """Raise GradeOutOfRangeError for invalid marks."""
    try:
        marks = float(input("Enter marks: "))
        if marks > 100:
            raise GradeOutOfRangeError("Marks cannot exceed 100!")
        print(f"Marks: {marks}")
    except GradeOutOfRangeError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid marks!")

def task_35_role_based_access():
    """Raise UnauthorizedAccessError for role check."""
    user_role = "guest"
    try:
        if user_role != "admin":
            raise UnauthorizedAccessError("Only admins can access this!")
        print("Access granted")
    except UnauthorizedAccessError as e:
        print(f"Error: {e}")

def task_36_file_format():
    """Raise InvalidFileFormatError for file uploader."""
    try:
        filename = input("Enter filename: ")
        if not filename.endswith('.txt'):
            raise InvalidFileFormatError("Only .txt files allowed!")
        with open(filename, 'r') as f:
            print(f.read())
    except InvalidFileFormatError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print("Error: File not found!")

def task_37_login_attempts():
    """Raise LoginAttemptsExceededError after 3 failed attempts."""
    attempts = 0
    correct_password = "pass123"
    while attempts < 3:
        try:
            password = input("Enter password: ")
            if password != correct_password:
                attempts += 1
                if attempts == 3:
                    raise LoginAttemptsExceededError("Too many failed attempts!")
                raise ValueError("Incorrect password!")
            print("Login successful")
            break
        except ValueError as e:
            print(f"Error: {e}")
        except LoginAttemptsExceededError as e:
            print(f"Error: {e}")
            logging.error(f"Login attempts exceeded: {e}")
            break

def task_38_object_state():
    """Class-level exception for object state."""
    class MyClass:
        def __init__(self, state):
            if state not in ['active', 'inactive']:
                raise ValueError("Invalid state!")
            self.state = state
    try:
        obj = MyClass("invalid")
    except ValueError as e:
        print(f"Error: {e}")

def task_39_file_too_large():
    """Raise FileTooLargeError for file validation."""
    try:
        filename = input("Enter filename: ")
        size = os.path.getsize(filename) if os.path.exists(filename) else 0
        if size > 1024:  # 1KB limit
            raise FileTooLargeError("File size exceeds 1KB!")
        with open(filename, 'r') as f:
            print(f.read())
    except FileTooLargeError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print("Error: File not found!")

def task_40_temperature_converter():
    """Raise InvalidTemperatureError for below absolute zero."""
    try:
        temp = float(input("Enter temperature in Kelvin: "))
        if temp < 0:
            raise InvalidTemperatureError("Temperature cannot be below absolute zero!")
        print(f"Temperature: {temp}K")
    except InvalidTemperatureError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid temperature!")

# Exception Handling in Loops and Functions (41–45)
def task_41_five_integers():
    """Collect 5 valid integers, handle bad inputs in loop."""
    numbers = []
    while len(numbers) < 5:
        try:
            num = int(input(f"Enter integer {len(numbers)+1}: "))
            numbers.append(num)
        except ValueError:
            print("Error: Invalid integer, try again!")
    print(f"Numbers: {numbers}")

def task_42_file_reader_function():
    """Function to read file with error handling."""
    def read_file(filename):
        try:
            with open(filename, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print("Error: File not found!")
            return None
    filename = input("Enter filename: ")
    content = read_file(filename)
    if content:
        print(content)

def task_43_recursive_factorial():
    """Handle exception in recursive factorial function."""
    def factorial(n):
        try:
            if n < 0:
                raise ValueError("Factorial not defined for negative numbers!")
            if n == 0:
                return 1
            return n * factorial(n - 1)
        except ValueError as e:
            print(f"Error: {e}")
            return None
    try:
        n = int(input("Enter number for factorial: "))
        result = factorial(n)
        if result is not None:
            print(f"Factorial: {result}")
    except ValueError:
        print("Error: Invalid number!")

def task_44_skip_bad_inputs():
    """Skip bad inputs in loop instead of crashing."""
    numbers = []
    for i in range(5):
        try:
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input, skipping...")
    print(f"Valid numbers: {numbers}")

def task_45_list_comprehension():
    """Try-except inside list comprehension."""
    inputs = [input(f"Enter number {i+1}: ") for i in range(5)]
    numbers = [int(x) for x in inputs if (lambda y: y.isdigit() or (y.startswith('-') and y[1:].isdigit()))(x)]
    print(f"Valid numbers: {numbers}")

# Real-Life Use Case Tasks (46–50)
def task_46_calculator():
    """Calculator with exception handling."""
    class InvalidOperationError(Exception):
        pass
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    try:
        a, op, b = input("Enter expression (e.g., 5 + 3): ").split()
        a, b = float(a), float(b)
        if op not in operations:
            raise InvalidOperationError("Invalid operator!")
        result = operations[op](a, b)
    except ValueError:
        print("Error: Invalid numbers!")
        logging.error("Invalid numbers in calculator")
    except ZeroDivisionError:
        print("Error: Division by zero!")
        logging.error("Division by zero in calculator")
    except InvalidOperationError as e:
        print(f"Error: {e}")
        logging.error(f"Invalid operation: {e}")
    else:
        print(f"Result: {result}")
    finally:
        print("Calculation complete")

def task_47_file_copy_tool():
    """File copy tool with error handling."""
    try:
        src = input("Enter source filename: ")
        dest = input("Enter destination filename: ")
        with open(src, 'r') as fsrc, open(dest, 'w') as fdest:
            content = fsrc.read()
            if not content:
                raise ValueError("Source file is empty!")
            fdest.write(content)
    except FileNotFoundError:
        print("Error: Source file not found!")
        logging.error("Source file not found")
    except PermissionError:
        print("Error: Permission denied!")
        logging.error("Permission denied")
    except ValueError as e:
        print(f"Error: {e}")
        logging.error(f"Empty file error: {e}")
    else:
        print("File copied successfully")
    finally:
        print("File copy operation complete")

def task_48_user_registration():
    """User registration with field validation."""
    class PasswordTooWeakError(Exception):
        pass
    try:
        name = input("Enter name: ")
        email = input("Enter email: ")
        age = int(input("Enter age: "))
        password = input("Enter password: ")
        assert isinstance(name, str) and isinstance(email, str), "Name and email must be strings!"
        assert age >= 13, "Age must be at least 13!"
        assert len(password) >= 8, "Password too weak!"
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise ValueError("Invalid email format!")
    except AssertionError as e:
        print(f"Error: {e}")
        logging.error(f"Registration error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
        logging.error(f"Registration error: {e}")
    else:
        print("Registration successful")
    finally:
        print("Registration attempt complete")

def task_49_log_exceptions():
    """App that logs exceptions to a file."""
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ValueError:
        logging.error("Invalid number input")
        print("Error: Invalid number!")
    except ZeroDivisionError:
        logging.error("Division by zero")
        print("Error: Division by zero!")
    else:
        print(f"Result: {result}")

def task_50_payment_gateway():
    """Payment gateway with error handling."""
    class PaymentError(Exception):
        pass
    balance = 500
    try:
        amount = float(input("Enter payment amount: "))
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        if amount > balance:
            raise PaymentError("Insufficient funds!")
        balance -= amount
    except ValueError:
        print("Error: Invalid amount!")
        logging.error("Invalid payment amount")
    except PaymentError as e:
        print(f"Error: {e}")
        logging.error(f"Payment error: {e}")
    else:
        print(f"Payment successful, new balance: {balance}")
    finally:
        print("Payment attempt complete")

# Run selected tasks for demonstration
if __name__ == "__main__":
    print("Running Task 46: Calculator")
    task_46_calculator()
    print("\nRunning Task 48: User Registration")
    task_48_user_registration()
    # Uncomment to test other tasks
    # task_1_divide_numbers()
    # task_2_validate_age()
    # ... etc.