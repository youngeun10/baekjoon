from sys import stdin

n = int(stdin.readline())
person = []

for _ in range(n):
    n, d, m, y = map(str, stdin.readline().split())
    person.append((n, int(y), int(m), int(d)))

person.sort(key=lambda x: (x[1], x[2], x[3]))

print(person[-1][0])
print(person[0][0])