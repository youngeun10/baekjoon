from sys import stdin

n = int(stdin.readline())
house = list(map(int, stdin.readline().rstrip().split()))
house.sort()
h_arr = {}
tmp = 0
tmp1 = [0] * n
for i in range(len(house)):
    h_arr[house[i]] = 0
    if i != 0:
        tmp += i * (house[i] - house[i-1])
        tmp1[i] = tmp

h_arr[house[-1]] = tmp1[-1]
tmp = 0
tmp2 = [0] * n
for i in range(len(house)-2, -1, -1):
    tmp += (n-i-1) * (house[i+1] - house[i])
    tmp2[i] = tmp
    h_arr[house[i]] = tmp1[i] + tmp2[i]
result = sorted(h_arr.items(), key=lambda x: x[1])
print(result[0][0])