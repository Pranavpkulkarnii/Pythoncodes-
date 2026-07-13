def evaluate_person(age, status, score):
    print(f"--- Evaluating: Age {age}, Status '{status}', Score {score} ---")
    
    # 1. Simple 'if' statement
    # Runs the block ONLY if the condition is True.
    if age >= 18:
        print("- You are legally an adult.")
        
    # 2. 'if-else' statement
    # Provides a fallback if the initial condition is False.
    if status == "student":
        print("- You qualify for the student discount.")
    else:
        print("- Regular pricing applies to you.")
        
    # 3. 'if-elif-else' ladder
    # Checks multiple conditions in order. The first True block runs.
    if score >= 90:
        print("- Grade: A")
    elif score >= 80:
        print("- Grade: B")
    elif score >= 70:
        print("- Grade: C")
    else:
        print("- Grade: Needs Improvement")
        
    # 4. Nested conditionals
    # An 'if' statement inside another 'if' statement for layered logic.
    if age >= 18:
        if status == "employed":
            print("- You are an employed adult. Don't forget your taxes!")
        else:
            print("- You are an adult, but not currently employed.")
            
    # 5. Inline Conditional (Ternary Operator)
    # A concise, one-line way to assign a value based on a condition.
    # Syntax: [value_if_true] if [condition] else [value_if_false]
    pass_status = "Passed" if score >= 50 else "Failed"
    print(f"- Exam Result: {pass_status}")
    
    # 6. Structural Pattern Matching (match-case)
    # Python's version of a "switch" statement (Requires Python 3.10+).
    match status:
        case "student":
            print("- Match: Focus on your upcoming exams.")
        case "employed":
            print("- Match: Hope work is going well.")
        case "retired":
            print("- Match: Enjoy your well-earned rest.")
        case _:  # The underscore acts as a wildcard/default case
            print("- Match: Status unrecognized.")
            
    print("\n") # Blank line for readability between tests

# --- Let's test the function with different scenarios ---

# Scenario 1: Adult student with a good score
evaluate_person(age=20, status="student", score=85)

# Scenario 2: Minor, not a student, failing score
evaluate_person(age=16, status="unemployed", score=45)

# Scenario 3: Employed adult with a perfect score
evaluate_person(age=30, status="employed", score=100)