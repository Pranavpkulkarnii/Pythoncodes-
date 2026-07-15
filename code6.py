# ==========================================
# 1. THE 'FOR' LOOP
# Used for iterating over a sequence (like a list, string, or range)
# ==========================================
print("--- For Loop (Iterating a List) ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\n--- For Loop (Using range) ---")
# range(1, 4) generates numbers 1, 2, 3 (stops before 4)
for i in range(1, 4):
    print(f"Number: {i}")


# ==========================================
# 2. THE 'WHILE' LOOP
# Executes a block of code as long as a condition is True
# ==========================================
print("\n--- While Loop ---")
count = 1
while count <= 3:
    print(f"Count is: {count}")
    count += 1  # Crucial: update the condition variable to avoid an infinite loop!


# ==========================================
# 3. LOOP CONTROL STATEMENTS
# Changing how the loops behave
# ==========================================
print("\n--- The 'break' Statement ---")
# 'break' stops the loop entirely
for num in range(1, 6):
    if num == 4:
        print("Hit 4, breaking the loop!")
        break
    print(num)

print("\n--- The 'continue' Statement ---")
# 'continue' skips the rest of the current iteration and moves to the next one
for num in range(1, 6):
    if num == 3:
        print("Skipping 3!")
        continue
    print(num)

print("\n--- The Loop 'else' Clause ---")
# The 'else' block runs ONLY if the loop finishes naturally (without hitting a 'break')
for i in range(3):
    print(f"Processing {i}...")
else:
    print("Loop completed successfully without interruptions.")