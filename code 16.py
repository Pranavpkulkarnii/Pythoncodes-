class Student:
    """A class representing a student."""
    
    def __init__(self, name, grade_level):
        # The __init__ method sets up the initial state of the object
        self.name = name
        self.grade_level = grade_level
        self.grades = [] # Every new student starts with an empty list of grades

    def add_grade(self, score):
        self.grades.append(score)

    def get_average(self):
        # Calculate the average grade, avoiding division by zero
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        # This determines how the object looks when you print() it
        return f"{self.name} (Grade {self.grade_level})"


class Teacher:
    """A class representing a teacher who manages multiple students."""
    
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = [] # The teacher starts with an empty roster

    def enroll_student(self, student):
        # This method takes a Student object and adds it to the teacher's list
        self.students.append(student)
        print(f"Enrolled {student.name} in {self.name}'s {self.subject} class.")

    def assign_grade(self, student_name, score):
        # Search through the teacher's students to find a match
        for student in self.students:
            if student.name == student_name:
                student.add_grade(score)
                print(f"Assigned a {score} to {student.name}.")
                return
        print(f"Error: {student_name} is not in this class.")

    def print_roster(self):
        print(f"\n--- {self.name}'s {self.subject} Roster ---")
        for student in self.students:
            print(f"{student} | Current Average: {student.get_average():.1f}")


# ==========================================
# Example Usage: Let's see the classes in action
# ==========================================

# 1. Create a Teacher object
mr_feeny = Teacher("Mr. Feeny", "History")

# 2. Create some Student objects
cory = Student("Cory Matthews", 10)
topanga = Student("Topanga Lawrence", 10)
shawn = Student("Shawn Hunter", 10)

# 3. The teacher enrolls the students
mr_feeny.enroll_student(cory)
mr_feeny.enroll_student(topanga)
mr_feeny.enroll_student(shawn)

# 4. The teacher assigns some grades
mr_feeny.assign_grade("Cory Matthews", 85)
mr_feeny.assign_grade("Cory Matthews", 78)

mr_feeny.assign_grade("Topanga Lawrence", 100)
mr_feeny.assign_grade("Topanga Lawrence", 98)

mr_feeny.assign_grade("Shawn Hunter", 70)

# 5. Print the final class roster to see everyone's averages
mr_feeny.print_roster()