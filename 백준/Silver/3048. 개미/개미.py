from sys import stdin

a, b = map(int, stdin.readline().split())
a_grp = list(stdin.readline().rstrip())
b_grp = list(stdin.readline().rstrip())
a_grp.reverse()
t = int(stdin.readline())

t_grp = a_grp + b_grp

for _ in range(t):
    for i in range(len(t_grp)-1):
        if t_grp[i] in a_grp and t_grp[i + 1] in b_grp:
            t_grp[i], t_grp[i + 1] = t_grp[i + 1], t_grp[i]

            if t_grp[i + 1] == a_grp[-1]:
                break

print("".join(t_grp))