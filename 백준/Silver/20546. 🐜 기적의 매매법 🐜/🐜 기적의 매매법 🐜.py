def BNP(s, d):
    c = 0
    for i in d:
        c += s // i
        s = s % i
    return c * d[-1] + s

def TIMING(s, d):
    c = 0
    chk = [0, ]
    for i in range(1, len(d)):
        if d[i-1] > d[i]:
            chk.append(-1)
        elif d[i-1] < d[i]:
            chk.append(1)
        else:
            chk.append(0)

        if i > 2:
            if sum(chk[i-2:i+1]) == 3:
                s += c * d[i]
                c = 0
            elif sum(chk[i-2:i+1]) == -3:
                c += s // d[i]
                s = s % d[i]
    return c * d[-1] + s

from sys import stdin
stock = int(stdin.readline())
days = list(map(int, stdin.readline().rstrip().split()))
if BNP(stock, days) > TIMING(stock, days): print("BNP")
elif BNP(stock, days) < TIMING(stock, days): print("TIMING")
else: print("SAMESAME")