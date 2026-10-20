# pyrefly: ignore [missing-import]
from collections import Counter
list = ["python", "java", " python", "cpp", "java", "python"]
fr = Counter(list)
print(fr)
print(fr["python"])





n = int(input())
arr = list(map(int, input().split()))

fre = {}
for num in arr:                    # loop over the elements
    if num in fre:
        fre[num] += 1
    else:
        fre[num] = 1

# Collect all frequency values
ans = []
for count in fre.values():
    ans.append(count)

# Check if all frequencies are unique
mod = set(ans)
print(len(ans) == len(mod))



from collections import Counter

skills = input().split()

# Use Counter to get the most common skill
skill_counts = Counter(skills)
most_common_skill, count = skill_counts.most_common(1)[0]

print(f"{most_common_skill}: {count}")