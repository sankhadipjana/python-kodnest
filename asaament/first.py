def is_happy_number(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        # Sum of the squares of the digits
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

if __name__ == "__main__":
    n = int(input().strip())
    print(is_happy_number(n))