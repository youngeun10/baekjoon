from sys import stdin

while True:
    a, b = map(int, stdin.readline().split())

    if a == 0 and b == 0:
        exit()
    print("Yes") if a > b else print("No")