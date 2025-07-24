# Use Case: Book tickets for passengers with constraints.
# Exception Handling Goals:
# Raise NoSeatsAvailableError
# Catch user errors (invalid ID, date)
# Use custom exceptions for frequent flyers
# Always log status with finally

import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='flight_booking_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class NoSeatsAvailableError(Exception):
    pass

class FrequentFlyerError(Exception):
    pass

def flight_booking():
    available_seats = 5
    bookings = []
    
    try:
        passenger_id = input("Enter passenger ID: ")
        if not passenger_id.isalnum():
            raise ValueError("Invalid passenger ID format")
            
        is_frequent_flyer = input("Are you a frequent flyer? (yes/no): ").lower() == 'yes'
        if is_frequent_flyer and len(passenger_id) < 5:
            raise FrequentFlyerError("Frequent flyer ID must be at least 5 characters")
            
        booking_date = input("Enter booking date (YYYY-MM-DD): ")
        booking_date = datetime.strptime(booking_date, '%Y-%m-%d')
        
        num_seats = int(input("Enter number of seats to book: "))
        if num_seats > available_seats:
            raise NoSeatsAvailableError("Not enough seats available")
            
        bookings.append((passenger_id, num_seats, booking_date))
        available_seats -= num_seats
        print(f"Booking confirmed for {num_seats} seats")
        
    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        print(f"Error: {str(ve)}")
        return False
    except NoSeatsAvailableError as nsae:
        logging.error(f"NoSeatsAvailableError: {str(nsae)}")
        print(f"Error: {str(nsae)}")
        return False
    except FrequentFlyerError as ffe:
        logging.error(f"FrequentFlyerError: {str(ffe)}")
        print(f"Error: {str(ffe)}")
        return False
    finally:
        logging.info(f"Booking attempt completed. Seats remaining: {available_seats}")
        print(f"Booking status: {'Success' if bookings else 'Failed'}")
        
    return bookings

if __name__ == "__main__":
    flight_booking()