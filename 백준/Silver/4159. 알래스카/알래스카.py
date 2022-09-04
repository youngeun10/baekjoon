from sys import stdin

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    else:
        arr = [int(stdin.readline().rstrip()) for _ in range(n)]
        arr.extend([0, 1422])
        tmp = sorted(arr)
        if tmp[-1] - tmp[-2] > 100:
            print("IMPOSSIBLE")
        else:
            m = tmp[1] - tmp[0]
            for i in range(2, n+2):
                if m < tmp[i] - tmp[i-1]:
                    m = tmp[i] - tmp[i-1]
            print("IMPOSSIBLE") if m > 200 else print("POSSIBLE")