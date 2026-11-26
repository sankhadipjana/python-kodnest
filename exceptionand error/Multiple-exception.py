# Default Exception Handler
# print("Program Started")
# a = 10
# print(a / 0) # Exception

# print("Program Ended")

# User Defined Exception Hndler

print("Program Started")
try:
    x = int(input("Enter the Number"))
    a = 10
    print(a / x) # Exception
    lst = [1, 2, 3, 4] # 0 1 2 3
    print(lst[2])
    # print(name) # NAME ERROR
except ZeroDivisionError:
    print("Cannot divide by Zero")
except IndexError:
    print("The Index is Out of the range")
except ValueError:
    print("Please enter Interger")
except Exception as e:
    print(e) # Gerenal Exception at last

print("Program Ended")






try:
    matche_skills = int(input())
    required_skills = int(input())

    percentage = (matche_skills / required_skills) * 100

except ValueError:
    print("Invalid skill count")

except ZeroDivisionError:
    print("Required skill cannot be zero")

else:
    print(percentage)

finally:
    print("Student profile processing is completed!")


#     Write Python programs for the following questions using built-in exceptions only. Do not create custom exception classes.

# 1. Safe Integer Conversion
# Read a value from the user and convert it into an integer. Handle ValueError if the input is not a valid integer.

try:
    value = int(input("Enter a number: "))
    print("Converted integer:", value)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
    
# 2. Safe Division Calculator
# Read two numbers and perform division. Handle ValueError for invalid input and ZeroDivisionError when the second number is zero.

# 3. Student Skill Lookup
# Given a list of skills:
# skills = ["Python", "SQL", "Java", "HTML"]
# Read an index and display the corresponding skill. Handle ValueError and IndexError.

# 4. Employee Details Lookup
# Store employee IDs and names in a dictionary. Read an employee ID and display the employee name. Handle KeyError if the employee ID does not exist.

# 5. Multiple Exception Handling
# Read two values and perform division. Handle ValueError, TypeError, and ZeroDivisionError using separate except blocks.

# 6. Student Marks Processing
# Read the number of subjects and their marks. Calculate the average using try, except, else, and finally. Handle invalid input and division by zero.

# 7. File Reading
# Open a file named student.txt and display its contents. Handle FileNotFoundError and use finally to print a completion message.

# 8. Positive Number Validation
# Read a number from the user. If the number is negative, raise a built-in ValueError. Handle the exception and print Negative numbers are not allowed.

# 9. Password Length Validation
# Read a password and check whether it contains at least 8 characters. Raise a built-in ValueError if the password is shorter than 8 characters.

# 10. Job Application Eligibility
# Read a candidate's percentage and check eligibility. If the percentage is below 60, raise a built-in ValueError. Handle invalid numeric input and display the appropriate message.