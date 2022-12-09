from sys import stdin

# n: 총 참가자 수 / m: 장르 수 / k: 최종 참가자 수
n, m, k = map(int, stdin.readline().split())
note = []

for i in range(m):
    tmp = list(map(str, stdin.readline().split()))
    for j in range(n):
        note.append([i+1, int(tmp[(2*j)]), float(tmp[(2*j)+1])])

note.sort(key=lambda x: (-x[2], x[1], x[0]))
cnt = 0
part = []
score = 0

for g, p, s in note:
    if p not in part:
        part.append(p)
        cnt += 1
        score += s
    if cnt == k:
        break
print(round(score, 1))