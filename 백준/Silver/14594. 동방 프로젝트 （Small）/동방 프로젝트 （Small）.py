from sys import stdin

n = int(stdin.readline())       # 동아리방 개수
m = int(stdin.readline())       # 빌런 행동 횟수
room = [1] * n

for _ in range(m):
    s, e = map(int, stdin.readline().split())
    for i in range(s, e):
        room[i] = 0
print(sum(room))