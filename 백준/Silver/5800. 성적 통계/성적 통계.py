from sys import stdin

for i in range(int(stdin.readline())):
    arr = list(map(int, stdin.readline().rstrip().split()))
    tmp = sorted(arr[1:], reverse=True)
    g = [tmp[j-1]-tmp[j] for j in range(1, len(tmp))]
    print(f"Class {i+1}")
    print(f"Max {max(arr[1:])}, Min {min(arr[1:])}, Largest gap {max(g)}")