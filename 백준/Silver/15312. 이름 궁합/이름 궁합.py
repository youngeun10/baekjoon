import sys
sys.setrecursionlimit(10**9)

def name(tArr, n):
    if n == 2:
        print(tArr[0], tArr[1], sep='')
        return 0

    arr = []

    for i in range(n - 1):
        arr.append((tArr[i] + tArr[i + 1]) % 10)

    return name(arr, n - 1)

alpha = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2
            , 'H': 3, 'I': 3, 'J': 2, 'K': 2, 'L': 1, 'M': 2, 'N': 2, 'O': 1, 'P': 2
            , 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
hap = list()

for i in range(len(a)):
    hap.append(alpha[a[i]])
    hap.append(alpha[b[i]])

name(hap, len(hap))
