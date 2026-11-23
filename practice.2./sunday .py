# class car:
#     def message(self):
#         print("hello")
#     def message2(self):
#         print("message2")    

# a= car()
# a.message() 
# a.message2()   

class calcul:
    def __init__(self,a,b,name):
        self.a = a
        self.b = b
        self.user_name=name
    def sum(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a - self.b)  
    def name(self):
        print(f"i am {self.user_name}")          

a = calcul(20,20,"sankha")

a.sum()
a.sub()
a.name()