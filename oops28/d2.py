class Student:
    # class attribute - directly classname or ref variable
    company = "kodnest"

    # Constructor
    def __init__(self, name, age):
        # Instance attributes - self or obj ref
        self.name = name
        self.age = age

    #Instance method - using self reference, obj ref
    def study(self):
        # a = 10 # Local attribute
        # print(a)
        print(f"{self.name} is studying")

    def getDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Company:", self.company)

    # classname or obj ref & no self or cls parameter
    @staticmethod
    def trip(name):
        print(f"{name} is going on a trip")

    # can use cls or ref variable, only cls is recommended for class methods
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


Student.change_company("Kodnest pvt lmt")
s1 = Student("Rahul", 20)
Student.trip(s1.name)
s1.trip(s1.name)
print(s1.name)
print(Student.company)
print(s1.company)
s1.study()
s1.getDetails()

print("\n")
s2 = Student("Priya", 22)
print(s2.name)
s2.study()
s2.getDetails()        