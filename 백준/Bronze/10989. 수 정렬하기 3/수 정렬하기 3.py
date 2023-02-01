import sys

input = sys.stdin.readline
print = sys.stdout.write

num_arr = [0] * 10001
for _ in range(int(input())):
    num_arr[int(input())] += 1

for i in range(1, 10001):
    if num_arr[i] > 0:
        for _ in range(num_arr[i]):
            print(str(i) + '\n')