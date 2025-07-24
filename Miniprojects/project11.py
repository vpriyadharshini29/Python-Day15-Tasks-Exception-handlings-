# Use Case: User answers multiple-choice questions.
# Exception Handling Goals:
# Catch wrong input types
# Use raise for answer outside A/B/C/D
# Track and log all exceptions
# Use loop + exception for multiple questions

import logging

# Configure logging
logging.basicConfig(filename='quiz_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidAnswerError(Exception):
    pass

def quiz_game():
    questions = [
        {"q": "What is 2+2?", "options": {"A": "3", "B": "4", "C": "5", "D": "6"}, "correct": "B"},
        {"q": "Color of the sky?", "options": {"A": "Blue", "B": "Red", "C": "Green", "D": "Yellow"}, "correct": "A"}
    ]
    score = 0
    
    for i, q in enumerate(questions, 1):
        try:
            print(f"\nQuestion {i}: {q['q']}")
            for option, value in q['options'].items():
                print(f"{option}: {value}")
                
            answer = input("Enter your answer (A/B/C/D): ").upper()
            if answer not in ['A', 'B', 'C', 'D']:
                raise InvalidAnswerError("Answer must be A, B, C, or D")
                
            if answer == q['correct']:
                score += 1
                print("Correct!")
            else:
                print(f"Wrong! Correct answer was {q['correct']}")
                
        except InvalidAnswerError as iae:
            logging.error(f"InvalidAnswerError for question {i}: {str(iae)}")
            print(f"Error: {str(iae)}")
        except Exception as e:
            logging.error(f"Unexpected error for question {i}: {str(e)}")
            print(f"Error: Unexpected issue - {str(e)}")
            
    print(f"\nFinal Score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()