def valid_parentheses(s):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in pairs.values():  # Opening brackets: '(', '[', '{'
            stack.append(char)
        elif char in pairs:         # Closing brackets: ')', ']', '}'
            # Invalid if stack is empty or top doesn't match expected opening bracket
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    # Valid only if all opening brackets were matched and popped
    return len(stack) == 0