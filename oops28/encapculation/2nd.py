# Access Modifiers -
# public - name anywhere
class Student:
    def __init__(self):
        self.name = "Rahul"

s = Student()
print(s.name)


# protected - _name class and subclass
class Student:
    def __init__(self):
        self._name = "Rahul"

class BioStudent(Student):
    def display(self):
        print(self._name)

bs = BioStudent()
bs.display()


# private __name - class getter and setter
class Student:
    def __init__(self):
        self.__name = "Rahul"

class BioStudent(Student):
    def display(self):
        pass
        # print(self.__name)

bs = BioStudent()
bs.display()
s = Student()
print(s._Student__name)