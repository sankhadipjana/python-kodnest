#function overloading is not allowed. The meaning of 
# function overloading is create two function with same name, 
# but multiple parameters. It's not allowed in Python. 





def sum(*a):
    sum = 0
    for i in a:
        sum+=i
    print(sum)    

sum(1,2,3,4,5,6,7)
sum(1,2,3)


# fincton recurtion
# Factorial of a number using recursion
# Example: fact(5) = 5 * 4 * 3 * 2 * 1 = 120
def fact(n):
    if n == 1:                  # Base case: factorial of 1 is 1
        return 1
    return n * fact(n - 1)      # Recursive case: n * fact(n-1)

print(fact(5))                  # Output: 120


# Fibonacci series using recursion
# Series: 0, 1, 1, 2, 3, 5, 8, 13, ...
# Example: fib(5) = 5
def fib(n):
    if n == 0:                  # Base case 1: fib(0) = 0
        return 0
    elif n == 1:                # Base case 2: fib(1) = 1
        return 1
    return fib(n - 1) + fib(n - 2)  # Recursive case: sum of previous two terms

print(fib(5))                   # Output: 5



def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Print first 10 Fibonacci numbers
for i in range(10):
    print(fib(i), end=" ")
