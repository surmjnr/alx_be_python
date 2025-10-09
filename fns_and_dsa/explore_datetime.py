"""
explore_datetime.py - A Python script demonstrating datetime module usage
This script shows how to work with dates and times in Python using the datetime module.
"""

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Display the current date and time in a readable format.
    
    Returns:
        datetime: The current date and time object
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format and print the current date and time
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    
    return current_date


def calculate_future_date(current_date, days_to_add):
    """
    Calculate a future date by adding specified days to the current date.
    
    Args:
        current_date (datetime): The starting date
        days_to_add (int): Number of days to add
    
    Returns:
        datetime: The future date
    """
    # Calculate the future date using timedelta
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    
    return future_date


def main():
    """
    Main function to run the datetime exploration program.
    """
    print("=== DateTime Exploration Program ===\n")
    
    # Part 1: Display current date and time
    print("Part 1: Current Date and Time")
    current_date = display_current_datetime()
    print()
    
    # Part 2: Calculate future date
    print("Part 2: Future Date Calculation")
    try:
        # Get user input for number of days
        days_input = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_input)
        
        # Calculate and display future date
        future_date = calculate_future_date(current_date, days_to_add)
        
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the program if this script is executed directly
if __name__ == "__main__":
    main()
