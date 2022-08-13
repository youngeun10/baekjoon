from sys import stdin
arr = stdin.readline().rstrip()
s = "UCPC"
c = 0
for i in arr:
    if i == s[c]:
        c += 1
        if c == 4:
            break
print("I love UCPC") if c == 4 else print("I hate UCPC")