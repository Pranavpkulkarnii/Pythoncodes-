def demonstrate_string_operations():
    print("--- 1-5: CHANGING CASE ---")
    s1 = "hello PYTHON world"
    print(f"1. capitalize() : {s1.capitalize()}")   # Capitalizes first letter only
    print(f"2. title()      : {s1.title()}")        # Capitalizes first letter of each word
    print(f"3. upper()      : {s1.upper()}")        # Converts all to uppercase
    print(f"4. lower()      : {s1.lower()}")        # Converts all to lowercase
    print(f"5. swapcase()   : {s1.swapcase()}")     # Swaps lower to upper and vice versa

    print("\n--- 6-8: TRIMMING WHITESPACE ---")
    s2 = "   Python   "
    print(f"Original        : '{s2}'")
    print(f"6. strip()      : '{s2.strip()}'")      # Removes spaces from both ends
    print(f"7. lstrip()     : '{s2.lstrip()}'")     # Removes spaces from the left end
    print(f"8. rstrip()     : '{s2.rstrip()}'")     # Removes spaces from the right end

    print("\n--- 9-11: SPLITTING AND JOINING ---")
    s3 = "apple,banana,cherry"
    # 9. split(): Splits string into a list based on a delimiter
    fruit_list = s3.split(",")
    print(f"9. split()      : {fruit_list}")
    
    # 10. splitlines(): Splits a string at line breaks
    s4 = "Line 1\nLine 2"
    print(f"10. splitlines(): {s4.splitlines()}")
    
    # 11. join(): Joins a list of strings into one string
    joined_fruits = " & ".join(fruit_list)
    print(f"11. join()      : {joined_fruits}")

    print("\n--- 12-16: SEARCHING AND REPLACING ---")
    s5 = "I love Python. Python is great!"
    # 12. replace(): Replaces all occurrences of a substring
    print(f"12. replace()   : {s5.replace('Python', 'Coding')}")
    
    # 13. find(): Returns lowest index of substring (-1 if not found)
    print(f"13. find()      : {s5.find('Python')}")
    
    # 14. rfind(): Returns highest index of substring (searching from right)
    print(f"14. rfind()     : {s5.rfind('Python')}")
    
    # 15. index(): Same as find(), but throws an error if not found
    print(f"15. index()     : {s5.index('love')}")
    
    # 16. count(): Counts how many times a substring appears
    print(f"16. count()     : {s5.count('Python')}")

    print("\n--- 17-23: BOOLEAN CHECKS (Returns True/False) ---")
    s6 = "Python2024"
    s7 = "12345"
    s8 = "hello"
    # 17. startswith(): Checks if string starts with specific characters
    print(f"17. startswith(): {s6.startswith('Py')}")
    
    # 18. endswith(): Checks if string ends with specific characters
    print(f"18. endswith()  : {s6.endswith('24')}")
    
    # 19. isalnum(): True if all characters are letters OR numbers
    print(f"19. isalnum()   : {s6.isalnum()}")
    
    # 20. isalpha(): True if all characters are letters ONLY
    print(f"20. isalpha()   : {s8.isalpha()}")
    
    # 21. isdigit(): True if all characters are numbers ONLY
    print(f"21. isdigit()   : {s7.isdigit()}")
    
    # 22. islower(): True if all letters are lowercase
    print(f"22. islower()   : {s8.islower()}")
    
    # 23. isupper(): True if all letters are uppercase
    print(f"23. isupper()   : {s8.isupper()}")

    print("\n--- 24-25: FORMATTING AND ALIGNMENT ---")
    s9 = "42"
    s10 = "Title"
    # 24. zfill(): Pads the string with zeros on the left until it reaches a specific length
    print(f"24. zfill()     : {s9.zfill(5)}")
    
    # 25. center(): Centers the string and pads it with a specific character
    print(f"25. center()    : {s10.center(15, '-')}")

# Run the demonstration
demonstrate_string_operations()