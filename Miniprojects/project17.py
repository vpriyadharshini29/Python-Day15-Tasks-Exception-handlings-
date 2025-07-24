# Use Case: Simulate calling external APIs.
# Exception Handling Goals:
# Simulate TimeoutError or ConnectionError
# Use custom InvalidResponseError
# Retry logic inside try-except loop
# Use finally to log attempts

import logging
import random
import time

# Configure logging
logging.basicConfig(filename='api_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidResponseError(Exception):
    pass

def simulate_api_call():
    max_retries = 3
    attempt = 0
    
    while attempt < max_retries:
        try:
            attempt += 1
            print(f"Attempt {attempt} to call API...")
            
            # Simulate random API issues
            rand = random.random()
            if rand < 0.3:
                raise TimeoutError("API call timed out")
            elif rand < 0.6:
                raise ConnectionError("Failed to connect to API")
            elif rand < 0.8:
                raise InvalidResponseError("Invalid response from API")
                
            print("API call successful!")
            return {"status": "success", "data": "Sample data"}
            
        except TimeoutError as te:
            logging.error(f"TimeoutError on attempt {attempt}: {str(te)}")
            print(f"Error: {str(te)}. Retrying...")
        except ConnectionError as ce:
            logging.error(f"ConnectionError on attempt {attempt}: {str(ce)}")
            print(f"Error: {str(ce)}. Retrying...")
        except InvalidResponseError as ire:
            logging.error(f"InvalidResponseError on attempt {attempt}: {str(ire)}")
            print(f"Error: {str(ire)}. Retrying...")
        finally:
            logging.info(f"API call attempt {attempt} completed")
            
        if attempt < max_retries:
            time.sleep(1)  # Wait before retry
            
    print("All retries failed")
    return None

if __name__ == "__main__":
    result = simulate_api_call()
    if result:
        print(f"Result: {result}")
        