# Use Case: Read and display content from a user-given file.
# Exception Handling Goals:
# Handle FileNotFoundError
# Raise PermissionError if file not readable
# Use finally to ensure file is closed
# Log all file errors
# Nested try block for open/read operations

import logging
import os

# Configure logging
logging.basicConfig(filename='file_reader_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def read_file(file_path):
    file = None
    try:
        # Nested try for file opening
        try:
            if not os.access(file_path, os.R_OK):
                raise PermissionError("File is not readable")
            file = open(file_path, 'r')
        except FileNotFoundError:
            logging.error(f"FileNotFoundError: File {file_path} not found")
            print(f"Error: File {file_path} not found")
            return None
        except PermissionError as pe:
            logging.error(f"PermissionError: {str(pe)}")
            print(f"Error: {str(pe)}")
            return None
        
        # Read file content
        content = file.read()
        
    except Exception as e:
        logging.error(f"Unexpected error while reading {file_path}: {str(e)}")
        print(f"Error: Unexpected issue occurred: {str(e)}")
        return None
    else:
        print("File content:")
        print(content)
        return content
    finally:
        if file is not None:
            file.close()
            print(f"File {file_path} closed")

if __name__ == "__main__":
    file_path = input("Enter the file path to read: ")
    read_file(file_path)