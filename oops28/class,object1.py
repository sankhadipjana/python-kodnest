class Student:
    # Properties (attributes) walways start with UPPER CASE
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks   

    # Behavior (methods)
    def study(self):
        print(f"{self.name} studies")

    def play(self):
        print("Student plays")


# Object creation
s = Student("sankha","32","85")     
s1 = Student("sachin","30","89")

print(s.name, s.age, s.marks)   # Output: Rahul 23 75

s.study()              # Output: Student studies
s.play()


print(s1.name,s1.marks,s1.age)  

s1.study()
s1.play()             # Output: Student plays