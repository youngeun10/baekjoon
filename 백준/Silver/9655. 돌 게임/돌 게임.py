import sys
input = sys.stdin.readline

N = int(input())
print("CY" if N % 2 == 0 else "SK")