try:
    # Code that might cause an error
    result = 10 / 0
except ZeroDivisionError:
    # What to do if THAT specific error happens
    print("Error: You cannot divide a number by zero!")