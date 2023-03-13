import sys
input = sys.stdin.readline

order = [list(map(str, input().split())) for _ in range(int(input()))]
st = []
result = []

for o in order:
    if o[0][0] == "t":
        result.append(st[-1]) if len(st) != 0 else result.append(-1)
    elif o[0][0] == "s":
        result.append(len(st))
    elif o[0][0] == "p" and len(o) == 1:
        result.append(st.pop()) if len(st) != 0 else result.append(-1)
    elif o[0][0] == "e":
        result.append(1) if len(st) == 0 else result.append(0)
    else:
        st.append(int(o[1]))

print(*result, sep="\n")