from sys import stdin

q = []

for _ in range(int(stdin.readline())):
    t = stdin.readline().strip()

    if "push_front" in t:
        q.insert(0, t[11:])
    elif "push_back" in t:
        q.append(t[10:])
    elif "pop_front" in t:
        print(q.pop(0)) if len(q) > 0 else print(-1)
    elif "pop_back" in t:
        print(q.pop(-1)) if len(q) > 0 else print(-1)
    elif "size" in t:
        print(len(q))
    elif "empty" in t:
        print(0) if len(q) > 0 else print(1)
    elif "front" in t:
        print(q[0]) if len(q) > 0 else print(-1)
    elif "back" in t:
        print(q[-1]) if len(q) > 0 else print(-1)