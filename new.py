try:
    user_input = "apple"
    number = int(123) # This will cause a ValueError
    result = 10 / number
except ValueError:
    print("Error: You must enter a valid number.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except Exception as e:
    # This catches any other unexpected errors and prints the exact error message
    print(f"An unexpected error occurred: {e}")