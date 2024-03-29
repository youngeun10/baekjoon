import sys

input = sys.stdin.readline
print = sys.stdout.write

st1 = list(input().strip())
st2 = list()

for _ in range(int(input())):
    c = input().strip()

    if 'L' in c:
        if st1:
            st2.append(st1.pop())
    elif 'D' in c:
        if st2:
            st1.append(st2.pop())
    elif 'B' in c:
        if st1:
            st1.pop()
    else:
        st1.append(c[2:])

print(''.join(st1) + ''.join(reversed(st2)))
