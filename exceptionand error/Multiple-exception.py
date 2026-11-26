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
    print(name) # NAME ERROR
except ZeroDivisionError:
    print("Cannot divide by Zero")
except IndexError:
    print("The Index is Out of the range")
except ValueError:
    print("Please enter Interger")
except Exception as e:
    print(e) # Gerenal Exception at last

print("Program Ended")