stu =list( ['sankha',34,"engeneering",34])
print(stu)
print(type(stu))

stu.append("6")
print(stu)

stu.pop(1)
print(stu)

fruits = ["apple", "mango", "banana", "Grapes", "kiwi"]
print (fruits)
print(len(fruits))
fruits.pop() #removes the last element fruits.pop(1) #removes element at index 1
fruits. remove ("Grapes")
del fruits #deletes the entire list
Fruits = ["apple", "mango", "banana", "Grapes", "kiwi"]
fruits.clear() #removes all the elements from the list but keep the list
print(fruits)
fruits = ["apple", "mango", "banana", "Grapes", "kiwi"]
fruits. append ("orange")
print(fruits)
fruits.insert (2, "cherry")


fruits. insert(2, "cherry")
print(fruits)
fruits. extend (["melon", "fig"])
print(fruits)
fruits[0] = "pineapple"
print(fruits)
fruits[1:4] = ["Kiwi", "Lemon", "Lime"]
print(fruits)



num = [10, 50, 20, 40, 30, 20]
num.sort() 
print (num) 
num.sort(reverse=True) 
print (num) 
num. reverse()
print (num)
c = num.count (20)
print(c)
idx = num.index(20)
print (idx)
#anumaret methood
