from sys import stdin
from collections import Counter

result = []
for _ in range(int(stdin.readline())):
    tmp = Counter(list(stdin.readline().rstrip()))
    
    if tmp not in result:
        result.append(tmp)

print(len(result))