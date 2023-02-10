from sys import stdin

a = [int(stdin.readline()) for _ in range(int(stdin.readline()))]

print("Junhee is not cute!") if a.count(1) < a.count(0) else print("Junhee is cute!")