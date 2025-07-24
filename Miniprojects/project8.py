# Use Case: Upload and validate CSV data.
# Exception Handling Goals:
# Handle FileNotFoundError, ValueError, and parsing issues
# Raise InvalidCSVFormatError
# Use try-except-else-finally for parsing and cleanup
# Log invalid rows

import logging
import csv

# Configure logging
logging.basicConfig(filename='csv_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidCSVFormatError(Exception):
    pass

def csv_uploader(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            
            if not header or len(header) < 2:
                raise InvalidCSVFormatError("CSV must have at least 2 columns")
                
            for row_num, row in enumerate(reader, start=2):
                try:
                    if len(row) != len(header):
                        raise InvalidCSVFormatError(f"Row {row_num} has incorrect number of columns")
                    # Example: expecting name (str) and score (float)
                    name, score = row
                    score = float(score)
                    data.append((name, score))
                except ValueError as ve:
                    logging.error(f"ValueError at row {row_num}: {str(ve)}")
                    print(f"Skipping row {row_num}: Invalid data")
                except InvalidCSVFormatError as icfe:
                    logging.error(f"InvalidCSVFormatError at row {row_num}: {str(icfe)}")
                    print(f"Skipping row {row_num}: {str(icfe)}")
                else:
                    print(f"Processed row {row_num}: {name}, {score}")
                    
    except FileNotFoundError:
        logging.error(f"FileNotFoundError: File {file_path} not found")
        print(f"Error: File {file_path} not found")
        return None
    except InvalidCSVFormatError as icfe:
        logging.error(f"InvalidCSVFormatError: {str(icfe)}")
        print(f"Error: {str(icfe)}")
        return None
    else:
        print("CSV processing completed successfully")
        return data
    finally:
        print("CSV upload attempt finished")
        
if __name__ == "__main__":
    file_path = input("Enter CSV file path: ")
    result = csv_uploader(file_path)
    if result:
        print("\nValid Data:")
        for name, score in result:
            print(f"{name}: {score}")