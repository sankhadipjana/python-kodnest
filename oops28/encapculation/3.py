# Encapsulation is a core idea in object-oriented programming (OOP).
# It bundles data (attributes) and the methods that operate on that data
# attr - Private(__), access (getters and setters), public, protected
# with encapsulation
class Bank:
    def __init__(self):
        self.__balance = 25000  # private variable

    # getter - read only attribute
    @property
    def get_balance(self):
        print(f"The balance is {self.__balance}")

    # setter
    # def setbalance(self, new_balance):
    #     if new_balance < 0:
    #         print("No balance")
    #     else:
    #         self.__balance = new_balance


b = Bank()
# print(b.__balance)  # not directly accessed (getter and setter)
# Name Mangling (objref._classname__attr)
print(b._Bank__balance)

b.get_balance


# __ -> private variable  # getter and setter or name mangling
# without Encapsulation
# class Bank:
#     def __init__(self, balance):
#         self.__balance = balance

# acc = Bank(50000)
# print(acc.balance)


class StudentProfile:
    def __init__(self, score):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score


student = StudentProfile(80)
student.score = 92
print(student.score)