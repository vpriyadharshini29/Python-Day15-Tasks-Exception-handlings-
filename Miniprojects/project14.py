# Use Case: Allow users to vote once per session.
# Exception Handling Goals:
# Raise AlreadyVotedError if user tries again
# Catch unexpected errors and log
# Use finally to display thanks message

import logging

# Configure logging
logging.basicConfig(filename='voting_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class AlreadyVotedError(Exception):
    pass

def voting_system():
    voted_users = set()
    
    while True:
        try:
            user_id = input("Enter your user ID (or 'exit' to finish): ")
            if user_id.lower() == 'exit':
                break
                
            if user_id in voted_users:
                raise AlreadyVotedError("User has already voted")
                
            vote = input("Enter your vote (A/B/C): ")
            if vote.upper() not in ['A', 'B', 'C']:
                raise ValueError("Invalid vote. Choose A, B, or C")
                
            voted_users.add(user_id)
            print(f"Vote recorded for user {user_id}: {vote}")
            
        except AlreadyVotedError as ave:
            logging.error(f"AlreadyVotedError: {str(ave)}")
            print(f"Error: {str(ave)}")
        except ValueError as ve:
            logging.error(f"ValueError: {str(ve)}")
            print(f"Error: {str(ve)}")
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            print("Error: An unexpected issue occurred")
        finally:
            print("Thank you for participating in the voting process!")
            
if __name__ == "__main__":
    voting_system()