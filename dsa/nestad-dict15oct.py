# ==========================================
# 1. Nested List: Student Marks
# ==========================================

# Create a nested list containing marks of students
student_marks = [
    [78, 85, 91],
    [72, 88, 80]
]

# Print the complete nested list
print("Student Marks:")
print(student_marks)

# Loop through each inner list
for m in student_marks:
    # Loop through each mark in the inner list
    for marks in m:
        print(marks)


# ==========================================
# 2. Dictionary: Students and Their Courses
# ==========================================

# Create a dictionary where:
# Key   = Course name
# Value = List of students enrolled in that course

students = {
    "Development": ["Abhi", "Ram", "Nitin"],
    "Testing": ["Karan", "Varun"],
    "DataAnalytics": ["Priya", "Radha"]
}

# Print the complete dictionary
print("\nStudent Details:")
print(students)

# Loop through each course and its student list
for course, student_list in students.items():

    # Print the course name
    print(f"\nCourse: {course}")

    # Print the label without moving to the next line
    print("Students: ", end="")

    # Loop through the students in the current course
    for student in student_list:
        # Print each student's name on the same line
        print(student, end=" ")

    # Move to the next line after printing all students
    print()

    # ==========================================
# 1. Print Students Using a For Loop
# ==========================================

students_list = ["Abhi", "Ram", "Nitin"]

# Print the heading on the same line
print("Students: ", end="")

# Loop through each student
for student in students_list:
    # Print each student's name on the same line
    print(student, end=" ")

# Move to the next line
print()


# ==========================================
# 2. Nested Dictionary: Student Information
# ==========================================

# Create a dictionary containing student details
# Each student has a Branch and Marks

students = {
    "Abhi": {
        "Branch": "Development",
        "Marks": 85
    },
    "Varun": {
        "Branch": "Testing",
        "Marks": 90
    }
}

# Print the complete dictionary
print("\nAll Student Details:")
print(students)


# ==========================================
# 3. Access Nested Dictionary Using Loops
# ==========================================

# Loop through each student and their information
for student, info in students.items():

    # Print the student's name
    print(f"\nStudent: {student}")

    # Loop through each key and value in the student's details
    for branch, marks in info.items():

        # Print the key and its corresponding value
        print(f"{branch}: {marks}")