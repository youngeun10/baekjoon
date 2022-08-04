from sys import stdin

dic = {}
grpCnt, quizCnt = map(int, stdin.readline().rstrip().split())
for _ in range(grpCnt):
    k = stdin.readline().rstrip()
    member = [stdin.readline().rstrip() for _ in range(int(stdin.readline().rstrip()))]
    dic[k] = sorted(member)

result = []

for _ in range(quizCnt):
    q = stdin.readline().rstrip()
    c = int(stdin.readline().rstrip())
    result.append(*[k for k, v in dic.items() if q in v]) if c == 1 else [result.append(a) for a in dic.get(q)]

print(*result, sep='\n')