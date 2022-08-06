import datetime

f = list(map(int, input().split()))
t = list(map(int, input().split()))

df = datetime.datetime(f[0], f[1], f[2])
dt = datetime.datetime(t[0], t[1], t[2])

gap = dt - df

print("gg") if gap.days > 365242 else print("D-"+str(gap.days))