from sys import stdin
nums = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
print(*sorted(nums), sep='\n')