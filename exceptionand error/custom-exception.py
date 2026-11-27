age = 5

if age <= 18:
    raise ValueError("Age cannot be negative or less than 18")

print("Age:", age)


age =5
if age!=5:
    raise TypeError

print("age:",age)    


class InvalidAgeException(Exception):
    pass

try:
    age = 25
    if age <= 18:
        raise InvalidAgeException("Invalid age cannot be negative or < 18")
    
    print("Age:", age)

except InvalidAgeException as e:
    print(e)

else:
    print("Valid age")

finally:
    print("Program ended")