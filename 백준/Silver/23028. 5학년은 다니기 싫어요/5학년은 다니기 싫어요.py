from sys import stdin
from collections import deque

n, a, b = map(int, stdin.readline().rstrip().split())
sub = deque(list(map(int, stdin.readline().rstrip().split())) for _ in range(10))
for _ in range(8-n):
    i, j = sub.popleft()
    a += i*3
    b += 6*3 if i+j > 6 else (i+j)*3 
print("Nice") if a >= 66 and b >= 130 else print("Nae ga wae")