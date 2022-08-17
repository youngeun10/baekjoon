from sys import stdin
input = stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]
score.sort()
gap = [abs((i+1) - score[i]) for i in range(n)]
print(sum(gap))