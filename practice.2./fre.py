# pyrefly: ignore [missing-import]
from collections import Counter
list = ["python", "java", " python", "cpp", "java", "python"]
fr = Counter(list)
print(fr)
print(fr["python"])


