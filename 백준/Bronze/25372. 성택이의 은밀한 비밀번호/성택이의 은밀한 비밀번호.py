from sys import stdin

for _ in range(int(stdin.readline())):
    pw = stdin.readline().rstrip()
    print("yes") if 6 <= len(pw) <= 9 else print("no")