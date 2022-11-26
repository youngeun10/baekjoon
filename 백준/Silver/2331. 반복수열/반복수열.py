from sys import stdin

a, p = map(int, stdin.readline().split())
d = [a]

while True:
    new = 0
    for i in (str(d[-1])):
        new += int(i) ** p
    if new in d:
        while True:
            if new == d.pop():
                print(len(d))
                exit()
    else:
        d.append(new)