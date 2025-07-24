# Use Case: Accept user input for date, guest count, etc.
# Exception Handling Goals:
# Raise OverBookingError if guests > rooms
# Validate date format
# Use multiple except blocks
# Use assert to ensure valid dates

import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='hotel_booking_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class OverBookingError(Exception):
    pass

def hotel_booking():
    available_rooms = 10
    max_guests_per_room = 4
    
    try:
        booking_date = input("Enter booking date (YYYY-MM-DD): ")
        # Validate date format
        booking_date = datetime.strptime(booking_date, '%Y-%m-%d')
        assert booking_date >= datetime.now(), "Booking date must be in the future"
        
        num_guests = int(input("Enter number of guests: "))
        num_rooms = int(input("Enter number of rooms: "))
        
        if num_guests > num_rooms * max_guests_per_room:
            raise OverBookingError("Too many guests for available rooms")
        if num_rooms > available_rooms:
            raise OverBookingError("Not enough rooms available")
            
    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        print(f"Error: Invalid input - {str(ve)}")
        return False
    except AssertionError as ae:
        logging.error(f"AssertionError: {str(ae)}")
        print(f"Error: {str(ae)}")
        return False
    except OverBookingError as obe:
        logging.error(f"OverBookingError: {str(obe)}")
        print(f"Error: {str(obe)}")
        return False
    else:
        print(f"Booking confirmed for {num_guests} guests in {num_rooms} rooms on {booking_date.date()}")
        return True
        
if __name__ == "__main__":
    hotel_booking()