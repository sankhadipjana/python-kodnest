print("Hashing")
print(hash(10))
print(hash("hello"))
print(hash(10.0))
print(hash((1,2,3)))

student = {
    "name": "Gamana",
    "age": 25,
    "course": "Python"
}
print(student["name"])
print(student["age"])

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

s1 = Student("Gamana", 25)
print(s1)
print(hash(s1))