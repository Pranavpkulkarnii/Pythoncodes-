# 1. Defining a basic function using 'def'
def greet_user(name):
    print(f"Hello, {name}! Welcome to functions.")

# Calling (using) the function
greet_user("Alice")
greet_user("Bob")

print("---")

# 2. Combining your new skill (functions) with your old skill (loops)
def print_multiples(number, times):
    print(f"The first {times} multiples of {number} are:")
    
    # A loop inside a function!
    for i in range(1, times + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

# Now you can run that entire block of looping code with just one line
print_multiples(5, 3) 
print("\nAnd again with different numbers:")
print_multiples(7, 4)