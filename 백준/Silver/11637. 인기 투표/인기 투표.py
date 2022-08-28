from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = [int(stdin.readline().rstrip()) for _ in range(n)]
    chk = -1
    tmp = sorted(arr, reverse=True)
    
    if tmp[0] > sum(arr) / 2:
        print(f"majority winner {arr.index(tmp[0])+1}")
    else:
        if arr.count(tmp[0]) > 1:
            print("no winner")
        else:
            print(f"minority winner {arr.index(tmp[0]) + 1}")