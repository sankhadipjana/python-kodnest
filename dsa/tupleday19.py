from _typeshed import importlib
from _typeshed import importlib
mytuple = (1, 2, 3, 4, 3, 3, 3)
print(mytuple[0:3])
print(mytuple.count (3))
print(mytuple.index(3))
print(mytuple, type(mytuple), len(mytuple))
#index

stu_info = ("Gamana", 12, 22.5, True)
print(stu_info, type(stu_info))
#index
print (stu_info[-1])
print (stu_info[1])
print (stu_info[2])
print (stu_info[-4])
# stu_info[®] = "Nithin" unchangeable
print(stu_info)


fruits = "apple", "mango", "guava", "banana",
print (fruits)
print(type(fruits))
for fruit in fruits:
   print (fruit)
names = ("Gamana", )
print(names, type(names))
# Constructor in Tuple
t = tuple ((1, 2, 3))
print(t, type(t))
t = tuple([1, 2, 3])
print(t, type(t))




t = tuple([1, 2, 3])
print(t, type(t))
mytup = (1, 2, 3, 4)
# mytup[2] = 3
# del mytup
# mytup. remove(3)
print(mytup)
num = (5, 6, 7)
mytup = mytup + num
# print(mytup.extend(num))
print(mytup)
# Unpacking of tuples

fruitslist = ("apple", "mango", "guava", "banana", "orange")
print (fruitslist)
f1, *f2, f3 = fruits
print (f1)
print(f2)
print(f3)



