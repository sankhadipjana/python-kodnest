num = int(input())

n = num
even_digit = []

while n > 0:
    digit = n % 10
    
    # Use continue to skip odd digits
    if digit % 2 != 0:
        n = n // 10
        continue
        
    even_digit.append(digit)
    n = n // 10

even_digit.reverse()

if len(even_digit) > 0:
    print(f"The even digits in {num} are:", *even_digit)
else:
    print(f"No even digits found in {num}.")





# 1. Prompt the user to enter a number and store it in num
num = input("Enter a number: ")

# Convert the input string to an integer for digit extraction
n = int(num)
total_sum = 0

# 2. Use a while loop to iterate through each digit of the number
while n > 0:
    digit = n % 10
    
    # 3. Use a continue statement to skip zero digits
    if digit == 0:
        n //= 10
        continue
    
    # 4. If a non-zero digit is found, add it to the running total
    total_sum += digit
    n //= 10

# 5. Print the total sum matching the sample output format
print(f"The sum of non-zero digits in {num} is: {total_sum}")