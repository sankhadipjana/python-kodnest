# s = "pythonprogrammming" 
# # travarce <--------------- this side
# print(s[-6:-1:-1])
# print(s[-6:-1:])
# print(s[::-2])
# print(s[::-1])
# print(s[-2:])
# print(s[2:-2]) #2:-2
# print(s[1:-2:2])
# print(s[-2:-12:-2])
# print(s[])
# print(s[])
# print(s[])
# print(s[])
# ============================================================

# STRING SLICING - NEGATIVE SLICING PRACTICE

# ============================================================

#

# Syntax:

# string[start:stop:step]

#

# Negative Index:

# -1 -> last character

# -2 -> second-last character

# -3 -> third-last character

#

# Rules:

# 1. Start is included

# 2. Stop is excluded

# 3. Negative index counts from the right

# 4. Negative step moves from right to left

#

# Try to predict the output before running each question.

# ============================================================





# ------------------------------------------------------------

# LEVEL 1 - BASIC NEGATIVE INDEXING

# ------------------------------------------------------------



# 1. Print the last character

text = "Python"

print(text[-1])





# 2. Print the second-last character

text = "Python"

print(text[-2])





# 3. Print the third-last character

text = "Programming"

print(text[-3])





# 4. Print the last four characters

text = "Developer"

print(text[-4:])





# 5. Print the last five characters

text = "Programming"

print(text[-5:])





# 6. Remove the last two characters

text = "Python"

print(text[:-2])





# 7. Remove the last three characters

text = "Programming"

print(text[:-3])





# 8. Extract everything except the last character

text = "Developer"

print(text[:-1])





# ------------------------------------------------------------

# LEVEL 2 - NEGATIVE START AND STOP

# ------------------------------------------------------------



# 9.

text = "Python"

print(text[-5:-2])





# 10.

text = "Programming"

print(text[-8:-3])





# 11.

text = "Developer"

print(text[-7:-2])





# 12.

text = "ABCDEFGHIJ"

print(text[-8:-3])





# 13.

text = "ABCDEFGHIJKLM"

print(text[-10:-5])





# 14.

text = "DataScience"

print(text[-8:-2])





# 15.

text = "FullStackDeveloper"

print(text[-12:-5])





# ------------------------------------------------------------

# LEVEL 3 - POSITIVE START + NEGATIVE STOP

# ------------------------------------------------------------



# 16.

text = "PythonProgramming"

print(text[2:-3])





# 17.

text = "DataScience"

print(text[2:-2])





# 18.

text = "FullStackDeveloper"

print(text[4:-4])





# 19.

text = "MachineLearning"

print(text[3:-3])





# 20.

text = "ProgrammingLanguage"

print(text[5:-5])





# ------------------------------------------------------------

# LEVEL 4 - NEGATIVE STEP

# ------------------------------------------------------------



# 21. Reverse the complete string

text = "Python"

print(text[::-1])





# 22. Reverse the complete string

text = "Programming"

print(text[::-1])





# 23. Take every second character from right to left

text = "ABCDEFGHIJ"

print(text[::-2])





# 24. Take every third character from right to left

text = "ABCDEFGHIJKL"

print(text[::-3])





# 25. Reverse part of the string

text = "ABCDEFGHIJ"

print(text[8:2:-1])





# 26. Reverse part of the string

text = "Programming"

print(text[8:2:-1])





# 27. Take every second character while moving backwards

text = "ABCDEFGHIJKL"

print(text[10:2:-2])





# 28. Take every third character while moving backwards

text = "ABCDEFGHIJKLMNO"

print(text[12:2:-3])





# ------------------------------------------------------------

# LEVEL 5 - NEGATIVE INDEX + NEGATIVE STEP

# ------------------------------------------------------------



# 29.

text = "ABCDEFGHIJ"

print(text[-1:-6:-1])





# 30.

text = "ABCDEFGHIJKL"

print(text[-2:-10:-2])





# 31.

text = "Programming"

print(text[-1:-8:-1])





# 32.

text = "PythonProgramming"

print(text[-2:-12:-2])





# 33.

text = "ABCDEFGHIJKLMNO"

print(text[-1:-10:-2])





# 34.

text = "ProgrammingLanguage"

print(text[-2:-15:-3])



text = "PythonProgramming"

print(text[-2:5:-1])





# 36.

text = "ABCDEFGHIJKLM"

print(text[10:2:-2])





# 37.

text = "Python"

print(text[-1:0:-1])





# 38.

text = "Programming"

print(text[-2:-9:-2])





# 39.

text = "ABCDEFGHIJKLMNO"

print(text[12:3:-3])





# 40.

text = "DataScienceWithPython"

print(text[-1:-15:-2])



# 41. What will be the output?

text = "Python"

print(text[-1:2])





# 42. What will be the output?

text = "Python"

print(text[1:-1])





# 43. What will be the output?

text = "Python"

print(text[-1:-1])





# 44. What will be the output?

text = "Python"

print(text[-10:-7])





# 45. What will be the output?

text = "Python"

print(text[-1:-7:-1])
