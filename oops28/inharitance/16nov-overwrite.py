# ============================================
# Example 1: Simple Method Overriding
# ============================================

class Parent:
    def marry(self):
        print("Marry at age 30")          # This is the overridden method


class Child(Parent):
    def marry(self):
        print("Marry at age 25")          # This is the overriding method
                                          # Child's version will be called instead of Parent's


c = Child()
c.marry()                                 # Output: Marry at age 25
                                          # (Child's method overrides Parent's method)


# ============================================
# Example 2: Method Overriding with Employee hierarchy
# ============================================

class Employee:
    def calculate_salary(self):
        print("Calculating employee salary")   # Base method (will be overridden)


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        basic_salary = 30000
        bonus = 5000
        print("Full Time Salary:", basic_salary + bonus)   # Overrides parent method


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        hours = 80
        rate = 200
        print("Part Time Salary:", hours * rate)           # Overrides parent method


# Creating objects
emp1 = FullTimeEmployee()
emp2 = PartTimeEmployee()

# Calling the overridden methods
emp1.calculate_salary()     # Output: Full Time Salary: 35000
emp2.calculate_salary()     # Output: Part Time Salary: 16000




class Employee:

    def calculate_salary(self):

        print("Calculating employee salary")





class FullTimeEmployee(Employee):

    def calculate_salary(self):

        basic_salary = 30000

        bonus = 5000

        print("Full Time Salary:", basic_salary + bonus)





class PartTimeEmployee(Employee):

    def calculate_salary(self):

        hours = 80

        rate = 200

        print("Part Time Salary:", hours * rate)





emp1 = FullTimeEmployee()

emp2 = PartTimeEmployee()



emp1.calculate_salary()

emp2.calculate_salary()