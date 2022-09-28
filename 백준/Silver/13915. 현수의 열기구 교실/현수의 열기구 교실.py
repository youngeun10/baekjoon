from sys import stdin

while True:
    try:
        n = int(stdin.readline())
        arr = list()

        for _ in range(n):

            a = list(stdin.readline().rstrip())
            a = set(a)

            if a not in arr:
                arr.append(a)

        print(len(arr))

    except Exception:
        break