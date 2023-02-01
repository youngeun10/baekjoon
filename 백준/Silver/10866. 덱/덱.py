import sys

input = sys.stdin.readline
print = sys.stdout.write

q = []

for _ in range(int(input())):
    t = input().strip()

    if "push_front" in t:
        q.insert(0, t[11:])
    elif "push_back" in t:
        q.append(t[10:])
    elif "pop_front" in t:
        print(q.pop(0) + '\n') if len(q) > 0 else print('-1' + '\n')
    elif "pop_back" in t:
        print(q.pop(-1) + '\n') if len(q) > 0 else print('-1' + '\n')
    elif "size" in t:
        print(str(len(q)) + '\n')
    elif "empty" in t:
        print(str(0) + '\n') if len(q) > 0 else print('1' + '\n')
    elif "front" in t:
        print(q[0] + '\n') if len(q) > 0 else print('-1' + '\n')
    elif "back" in t:
        print(q[-1] + '\n') if len(q) > 0 else print('-1' + '\n')