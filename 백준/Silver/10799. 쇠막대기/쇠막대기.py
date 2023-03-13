import sys
input = sys.stdin.readline

bar = input()
newBar = bar.replace("()", "-")
cnt = 0
result = 0
for b in newBar:
    if b == "(":
        cnt += 1
    elif b == ")":
        cnt -= 1
        result += 1
    else:
        result += cnt
print(result)