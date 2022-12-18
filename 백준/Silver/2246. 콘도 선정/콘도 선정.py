from sys import stdin

n = int(stdin.readline())
arr = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
result = [0] * n

# x보다 바닷가에서 더 가까운 콘도들은 모두 x보다 숙박비가 더 비싸다
# x보다 숙박비가 더 싼 콘도들은 모두 x보다 바닷가에서 더 멀다

for i in range(n):
    c1, c2 = 0, 0
    d1, d2 = 0, 0
    for j in range(n):
        if i == j:
            pass
        # 거리
        if arr[i][0] > arr[j][0]:
            c1 += 1
            if arr[i][1] < arr[j][1]:
                c2 += 1
        # 가격
        if arr[i][1] > arr[j][1]:
            d1 += 1
            if arr[i][0] < arr[j][0]:
                d2 += 1
    result[i] = 1 if c1 == c2 and d1 == d2 else 0

print(sum(result))