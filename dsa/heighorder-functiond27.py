 
numbers = [1, 2, 3, 4, 5]
#Square numbers using HOF - map 
def square (n):
 return n * n    
result = map(square, numbers)
print(list(result))
#Even - filter 
def is_even (x):
  if x % 2 == 0: 
    return True
  else:
    return False
even_num = filter(is_even, numbers)
print(list(even_num))
# sum - reduce
from functools import reduce 
def add (x,y) :
  return x + y
sum_of_num=reduce (add, numbers)
print (sum_of_num)


# Lambda function
numbers_1 = [1, 2, 3, 4, 5]
result = map(lambda x : x * x, numbers_1)
print(list(result))
even = filter(lambda x : x % 2 == 0, numbers_1)
print(list(even))
sum = reduce(lambda x, y : x + y, numbers_1)
print (sum)
# Syntax => lambda arguments: expression-