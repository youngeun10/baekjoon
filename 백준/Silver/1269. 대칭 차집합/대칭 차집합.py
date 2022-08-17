from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
a = (map(int, stdin.readline().rstrip().split()))
b = (map(int, stdin.readline().rstrip().split()))
print(len(set(a) ^ set(b)))