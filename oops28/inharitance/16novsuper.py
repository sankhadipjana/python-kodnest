# Parent class
class Parent:
    def __init__(self, pname):
        self.pname = pname          # Initialize parent's name attribute

    def show(self):
        print("Parent method")      # Method that will be inherited / overridden


# Child class inherits from Parent
class child(Parent):
    def __init__(self, cname, pname):
        self.cname = cname          # Initialize child's own name attribute
        super().__init__(pname)     # Call Parent's __init__ using super()
                                    # This sets self.pname = pname

    def show(self):
        super().show()              # First call the Parent's show() method
        print("Child method")       # Then execute the child's own code


# Create an object of the child class
c = child("Ganesha", "Shiva")

print(c.cname)      # Output: Ganesha
print(c.pname)      # Output: Shiva  (inherited from Parent)
c.show()            # Output:
                    # Parent method
                    # Child method

# Note: super() always refers to the parent class