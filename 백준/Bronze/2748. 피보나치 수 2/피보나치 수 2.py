import sys
input = sys.stdin.readline

# fibonacci(0부터 시작): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ... 
fibo = [0, 1]
N = int(input())

for i in range(2, N+1):
    fibo.append(fibo[i-2]+fibo[i-1])

print(fibo[N])