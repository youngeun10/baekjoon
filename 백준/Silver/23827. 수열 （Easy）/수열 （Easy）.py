from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().rstrip().split()))
s_arr = sum(arr)
result = 0

for i in arr:
    s_arr -= i
    result += i*s_arr
print(result % 1000000007)