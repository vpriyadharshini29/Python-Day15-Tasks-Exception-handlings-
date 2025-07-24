# Use Case: Let user add products and prices, calculate total.
# Exception Handling Goals:
# Catch invalid price entries (ValueError)
# Raise custom ProductExistsError for duplicates
# Use finally to display total no matter what

import logging

# Configure logging
logging.basicConfig(filename='cart_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ProductExistsError(Exception):
    pass

def shopping_cart():
    cart = {}
    total = 0.0
    
    while True:
        try:
            product = input("Enter product name (or 'done' to finish): ")
            if product.lower() == 'done':
                break
                
            if product in cart:
                raise ProductExistsError(f"Product {product} already in cart")
                
            price = float(input(f"Enter price for {product}: "))
            if price < 0:
                raise ValueError("Price cannot be negative")
                
            cart[product] = price
            total += price
            
        except ValueError as ve:
            logging.error(f"ValueError: {str(ve)}")
            print(f"Error: Invalid price entered - {str(ve)}")
        except ProductExistsError as pee:
            logging.error(f"ProductExistsError: {str(pee)}")
            print(f"Error: {str(pee)}")
        finally:
            print(f"Current total: ${total:.2f}")
    
    return cart, total

if __name__ == "__main__":
    cart, total = shopping_cart()
    print("\nFinal Cart:")
    for product, price in cart.items():
        print(f"{product}: ${price:.2f}")
    print(f"Total: ${total:.2f}")