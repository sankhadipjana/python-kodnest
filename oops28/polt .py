# Class representing a Cat
class Cat:
    def sound(self):
        print("Cat Meow")

# Class representing a Cow
class Cow:
    def sound(self):
        print("Cow Moos")

# Function that demonstrates polymorphism
# It accepts any object that has a sound() method
def make_sound(animal):
    animal.sound()

# Create objects
c = Cat()
cow = Cow()

# Call the same function with different objects
make_sound(c)    # Output: Cat Meow
make_sound(cow)  # Output: Cow Moos