# ==========================================
# 1. WITHOUT EXCEPTION HANDLING (Will stop at the first error)
# ==========================================
# a = 10
# c = 6 / 0              # ZeroDivisionError
# print(c)

# stu_info = {"name": "Ram", "age": 22}
# print(stu_info["salary"])  # KeyError

# lst = [2, 4, 6]
# print(lst[4])            # IndexError

# print(age)               # NameError (if 'age' is not defined)

# a = 10
# b = "20"
# print(a + b)             # TypeError

# num = int("hello")       # ValueError
# print(num)


# ==========================================
# 2. WITH EXCEPTION HANDLING (try - except)
# ==========================================

# ZeroDivisionError
try:
    a = 10
    c = 6 / 3
    print(c)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# KeyError
stu_info = {"name": "Ram", "age": 22}
try:
    print(stu_info["salary"])
except KeyError:
    print("There is no key called salary.")

# IndexError
lst = [2, 4, 6]
try:
    print(lst[4])
except IndexError:
    print("Index is out of range for the list.")

# NameError
try:
    print('age')
except NameError:
    print("Variable is not declared before use.")

# TypeError
try:
    x = 10
    y = "20"
    print(x + y)
except TypeError:
    print("Cannot add an integer and a string directly.")

# ValueError


try:
    num = int("hello")
    print(num)
except ValueError:
    print("Invalid literal for int(): cannot convert 'hello' to an integer.")