from sys import stdin
from collections import deque

def chkstr(st, tt):

    sd = deque(st)
    chk = sd.popleft()

    for i in tt:
        if chk == i:
            if len(sd) == 0:
                return "Yes"
            chk = sd.popleft()
    return "No"


while True:
    try:
        s, t = map(str, stdin.readline().split())

        if s in t:
            print("Yes")
        else:
            print(chkstr(s, t))

    except Exception:
        break