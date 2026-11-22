
# Encapsulation is a core idea in object-oriented programming (OOP).
# It bundles data (attributes) and the methods that operate on that data into a single unit called a class.
# attr - Private(__), access (getters and setters), public, protected(_)

# With Encapsulation

class Bank:

    def __init__(self):
        self.__balance = 25000  # Private variable

    # Getter
    def get_balance(self):
        print(f"The balance is {self.__balance}")

    # Setter
    def set_balance(self, new_balance):
        if new_balance < 0:
            print("No balance")
        else:
            self.__balance = new_balance


b = Bank()

# print(b.__balance)  # Not directly accessible (getter and setter)

# Name Mangling (object._classname__attribute)
print(b._Bank__balance)

b.get_balance()

b.set_balance(100000)

b.get_balance()


# Private variable - getter and setter or name mangling

# Without Encapsulation

# class Bank:
#     def __init__(self, balance):
#         self.__balance = balance

# acc = Bank(50000)
# print(acc.balance)