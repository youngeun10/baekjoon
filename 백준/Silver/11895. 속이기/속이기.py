from sys import stdin
n = int(stdin.readline())
card = list(map(int, stdin.readline().rstrip().split()))
chk = 0
card.sort()
for i in card:
    chk = chk ^ i
print(sum(card)-card[0]) if chk == 0 else print(0)