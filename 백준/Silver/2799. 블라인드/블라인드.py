from sys import stdin

m, n = map(int, stdin.readline().split())   # 층 개수 / 층별 창문 개수
arr = [stdin.readline().rstrip() for _ in range((5*m)+1)]

blind = {0: ["....", "....", "....", "...."]
         , 1: ["****", "....", "....", "...."]
         , 2: ["****", "****", "....", "...."]
         , 3: ["****", "****", "****", "...."]
         , 4: ["****", "****", "****", "****"]}
window = []
result = [0] * 5

for i in range(m):
    for j in range(n):
        tmp = []
        tmp.append(arr[(5 * i) + 1][(5 * j) + 1:(5 * (j + 1))])
        tmp.append(arr[(5 * i) + 2][(5 * j) + 1:(5 * (j + 1))])
        tmp.append(arr[(5 * i) + 3][(5 * j) + 1:(5 * (j + 1))])
        tmp.append(arr[(5 * i) + 4][(5 * j) + 1:(5 * (j + 1))])
        window.append(tmp)

for i in window:
    if i == blind[0]: result[0] += 1
    if i == blind[1]: result[1] += 1
    if i == blind[2]: result[2] += 1
    if i == blind[3]: result[3] += 1
    if i == blind[4]: result[4] += 1

print(*result)