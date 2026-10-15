# =====================================================
# 1. Count Frequency Manually Using a Dictionary
# =====================================================

languages = ["Python", "Java", "Python", "SQL", "Java", "Python"]

# Create an empty dictionary to store frequencies
frequency = {}

# Loop through each language
for language in languages:

    # Check whether the language already exists
    if language in frequency:
        # Increase its count by 1
        frequency[language] += 1
    else:
        # If it does not exist, initialize its count to 1
        frequency[language] = 1

# Print the frequency dictionary
print("Manual Frequency Count:", frequency)


# =====================================================
# 2. Count Frequency Using Counter()
# =====================================================

# Import Counter from the collections module
from collections import Counter

languages = ["Python", "Java", "Python", "SQL", "Java", "Python"]

# Count the occurrences of each language automatically
frequency = Counter(languages)

# Print the count of Python
print("Python Count:", frequency["Python"])

# Print the count of Java
print("Java Count:", frequency["Java"])


# =====================================================
# 3. Display Each Language and Its Frequency
# =====================================================

languages = ["Python", "Java", "Python", "SQL"]

# Create a Counter object
frequency = Counter(languages)

# .items() returns each language and its count
for language, count in frequency.items():

    # Print the language and its frequency
    print(language, count)


# =====================================================
# 4. Count the Frequency of Letters in a String
# =====================================================

# Counter can also count individual characters
letter_counts = Counter("banana")

# Print the frequency of each character
print("Letter Counts:", letter_counts)


# =====================================================
# 5. Find the Most Common Skill
# =====================================================

skills = [
    "Python",
    "Java",
    "Python",
    "SQL",
    "Java",
    "Python"
]

# Count how many times each skill appears
skill_counts = Counter(skills)

# Print the frequency of all skills
print("Skill Counts:", skill_counts)

# Find all skills sorted by frequency, from highest to lowest
frequent_skills = skill_counts.most_common()

# Print the complete frequency ranking
print("All Frequent Skills:", frequent_skills)


# =====================================================
# 6. Find the Single Most Common Skill
# =====================================================

# most_common(1) returns a list containing the most common item
most_required = skill_counts.most_common(1)

# Extract the skill name
skill = most_required[0][0]

# Extract the skill's frequency
count = most_required[0][1]

# Print the most common skill and its count
print("Most Common Skill:", skill)
print("Frequency:", count)