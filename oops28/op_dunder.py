# # oPERATOR OVERLOADING - dunder methods, magic methods __add__

print(3 + 5)  # 8
print("gamana" + "Reddy")

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return Student(self.marks + other.marks)

s1 = Student(85)
s2 = Student(90)
print(s1, s2)

res = s1 + s2
print(res.marks)  # 175


class Person:
    def __init__(self, name, marks):
        self.name = name
        self.age = marks   # note: attribute is named 'age' but stores marks

    def __gt__(self, other):
        return self.marks > other.marks   # bug: should be self.age

p1 = Person("Ram", 30)
p2 = Person("Avi", 40)

if p1 > p2:
    print(f"{p1.name} scores highest marks")
else:
    print(f"{p2.name} scores highest marks")


# len
print(len("smitha"))  # 6
l1 = [1, 2, 3]
print(len(l1))  # 3

d1 = {
    "name": "Ram"
}
print(len(d1))  # 1