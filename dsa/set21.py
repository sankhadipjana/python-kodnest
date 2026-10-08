
s = {1, 2, 3, 4, 5, 3.56, "Hello", "Hello", 1, 0,}
print (s) # Output: {0, 1, 2, 3, 4, 5, 2.0, 3.56, print(type(s)) # Output: ‹class 'set'›
set1 = {'apple', "mango", 'banana', 'orange'}
# set1[2] = "pineapple"
set1.add("Pineapple")
print(set1)
set1.update(["Kiwi", "Grapes"])
set1.remove( "banana")
set1.discard( "kiwi")
set1.pop()
set1.clear()
print (set1)
del set1
# print (set1)

print(type(s)) # Output: ‹class 'set'>
set1 = {'apple', 'mango', 'banana', 'orange'}
# set1[2] = "pineapple"
set1. add("Pineapple")
print(set1)
set1.update(["Kiwi", "Grapes"])
set1.remove( "banana") 
set1.discard("kiwi")
set1.pop ()
set1.clear()
print (set1)
del set1
# print (set1)
#Constructor
names = set (["Abhi", "Gamana"])
print (names) 
for n in names:
    print (n)

#frozenset
fs = frozenset({1,2,3,4})
print(fs,type(fs))     