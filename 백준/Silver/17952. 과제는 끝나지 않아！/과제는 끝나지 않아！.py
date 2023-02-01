from sys import stdin

score = 0
st = []
tmp = []

for _ in range(int(stdin.readline())):
    c = list(map(int, stdin.readline().split()))

    if c[0] == 1:
        if c[2] - 1 == 0:
            score += c[1]
        else:
            st.append([c[1], c[2]-1])
    else:
        if len(st) > 0:
            tmp = st.pop()
            if tmp[1] - 1 == 0:
                score += tmp[0]
            else:
                st.append([tmp[0], tmp[1]-1])

print(score)