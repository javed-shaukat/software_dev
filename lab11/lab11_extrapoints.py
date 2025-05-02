"""
Javed Shaukat
Lab 11, Class in Python. (Extra Points)
"""

class Student:
    def __init__(self, name, age):
        # Initialize attributes here
        self.name = name
        self.age = age
        self.grade = {}  # Initialize empty dictionary for grades
    
    def add_grade(self, subject, grade):
        # Implement method to add grade
        self.grade[subject] = grade
    
    def get_average_grade(self):
        # Implement method to calculate average grade
        if not self.grade:  # if dictionary is empty
            return 0.0
        return sum(self.grade.values()) / len(self.grade)

# CALLING THE CLASS
# Create instances and demonstrate usage of each method

# Create student instances
student1 = Student("Alice Johnson", 18)
student2 = Student("Tyler Smith", 17)

# Add grades for student1
student1.add_grade("Math", 90.5)
student1.add_grade("Science", 93.0)
student1.add_grade("History", 92.5)

# Add grades for student2
student2.add_grade("Math", 89.0)
student2.add_grade("Science", 92.5)
student2.add_grade("History", 91.0)

# Demonstrate getting average grades
print(f"{student1.name}'s average grade: {student1.get_average_grade():.2f}")
print(f"{student2.name}'s average grade: {student2.get_average_grade():.2f}")

# Add another grade and show updated average
student1.add_grade("English", 94.0)
print(f"\nAfter adding English grade, {student1.name}'s new average: {student1.get_average_grade():.2f}")
student2.add_grade("English", 87.0)
print(f"\nAfter adding English grade, {student2.name}'s new average: {student2.get_average_grade():.2f}")

# Show all grades for Student 1
print(f"\n{student1.name}'s grades:")
for subject, grade in student1.grade.items():
    print(f"{subject}: {grade}")

# Show all grades for Student 2
print(f"\n{student2.name}'s grades:")
for subject, grade in student2.grade.items():
    print(f"{subject}: {grade}")