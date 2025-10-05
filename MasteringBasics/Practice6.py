from collections import defaultdict
b = [1, 1, 2]

s = defaultdict(int)
for i in b:
    s[i] += 1


print(s(1))