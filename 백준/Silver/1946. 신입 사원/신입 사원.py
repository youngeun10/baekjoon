from sys import stdin

for _ in range(int(stdin.readline().rstrip())):
    testCase = int(stdin.readline().rstrip())
    intern = []
    for _ in range(testCase):
        a, b = map(int, stdin.readline().rstrip().split())
        intern.append((a, b))
    intern.sort(key=lambda x: x[0])
    cnt = 1
    rank = intern[0][1]
    for i in range(1, testCase):
        cur = intern[i][1]
        if cur < rank:
            rank = cur
            cnt += 1
    print(cnt)