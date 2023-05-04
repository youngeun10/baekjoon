import sys
input = sys.stdin.readline

extension = {}

for _ in range(int(input())):
    tmp = list(map(str, input().rstrip().split('.')))

    if tmp[1] not in extension:
        extension[tmp[1]] = 1
    else:
        extension[tmp[1]] += 1

result = sorted(extension.items(), key=lambda x: x[0])

for e, n in result:
    print(e, n)