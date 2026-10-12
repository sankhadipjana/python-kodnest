# Square
square=[]
for i in range (1, 6):
    square. append(i * i)
print (square)


square = [i * i for i in range (1, 6)]
print (square)


numbers = [i for i in range(1, 11) if i % 2 == 0]
print (numbers)


number = [10, 3, 12, 5, 43, 7]
new_list = [i for i in number if i >= 10] 
print (new_list)


names = ["ravi", "abhi", "sita", "geeta", "mona"]
new_list = [name.upper() for name in names]
print (new_list)


print("cube of a number")
cube = [i*i*i for i in range(1,11)]
print(cube)

ps = [1,2,4,-5,-4,2]
psans = [i for i in ps if i > 0 ]
print(psans)


words = ["Apple", "Banana", "Orange", "Grapes", "Umbrella"]
result = [i for i in words if i[0].lower() in "aeiou"]
print(result)


numbers = range(1, 11)
result = ["Even" if i % 2 == 0 else "Odd" for i in numbers]
print(result)


text = "programming"
result = [i for i in text if i in "aeiou"]
print(result)


words = ["Python", "Java", "React", "Django"]
result = [len(word) for word in words]
print(result)



nums = [1, 2, 3, 2, 4, 1, 5]
result = []
[result.append(i) for i in nums if i not in result]
print(result)


matrix = [[1, 2], [3, 4], [5, 6]]
result = [num for row in matrix for num in row]
print(result)



a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
result = [i for i in a if i in b]
print(result)



prime = [n for n in range(2, 101) if all(n % i != 0 for i in range(2, n))]
print(prime)