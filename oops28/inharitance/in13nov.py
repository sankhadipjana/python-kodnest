class Father:

    def show(self):

        print("Father Method")
class Mother:

    def show(self):

        print("Mother Method")
class Child(Father, Mother):
    pass
c = Child()

c.show()

print(Child.mro())
