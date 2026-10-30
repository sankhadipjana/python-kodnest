# from __unknown__ import val
chars = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c']

freq = {}
for char in chars:
    freq[char] = freq.get(char, 0) + 1
fin = []
for key ,value in freq.items():
    fin.append(key)
    if value > 1:
        fin.append((value))

print(len(fin))    



