def Brute_Force(idx, x, y):
    global answer
    if idx == m:
        choice_chichen = []
        for i in range(n):
            for j in range(n):
                if City[i][j] == 3:
                    choice_chichen.append((i, j))
        res = Min_Distance(choice_chichen, house)
        if answer > sum(res):
            answer = sum(res)
        return
    else:
        for i in range(x, n):
            if i == x: k = y
            else: k = 0
            for j in range(k, n):
                if City[i][j] == 2:
                    City[i][j] = 3
                    Brute_Force(idx+1, i, j+1)
                    City[i][j] = 2

def Min_Distance(chichen, house):
    sum_Distance = []
    for i in house:
        min_D = 10 ** 9
        for j in chichen:
            Distance = abs(i[0]-j[0]) + abs(i[1]-j[1])
            min_D = min(min_D, Distance)
        sum_Distance.append(min_D)
    return sum_Distance


n, m = map(int, input().split())
City = [list(map(int, input().split())) for _ in range(n)]
answer = 10 ** 9
house = []
for i in range(n):
    for j in range(n):
        if City[i][j] == 1:
            house.append((i, j))
Brute_Force(0, 0, 0)
print(answer)