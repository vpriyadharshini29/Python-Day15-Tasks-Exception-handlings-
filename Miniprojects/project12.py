# Use Case: User guesses a random number.
# Exception Handling Goals:
# Catch non-numeric guesses
# Raise GameOverError after 5 failed attempts
# Use try-except-finally for turn logic

import logging
import random

# Configure logging
logging.basicConfig(filename='guessing_game_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class GameOverError(Exception):
    pass

def number_guessing_game():
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess the number (1-100), attempt {attempts+1}/{max_attempts}: "))
            attempts += 1
            
            if attempts == max_attempts and guess != target:
                raise GameOverError("Maximum attempts reached")
                
            if guess == target:
                print("Congratulations! You guessed correctly!")
                return True
            elif guess < target:
                print("Too low!")
            else:
                print("Too high!")
                
        except ValueError as ve:
            logging.error(f"ValueError: {str(ve)}")
            print("Error: Please enter a valid number")
        except GameOverError as goe:
            logging.error(f"GameOverError: {str(goe)}")
            print(f"Game Over! The number was {target}")
            return False
        finally:
            print(f"Attempts used: {attempts}")
            
    return False

if __name__ == "__main__":
    number_guessing_game()