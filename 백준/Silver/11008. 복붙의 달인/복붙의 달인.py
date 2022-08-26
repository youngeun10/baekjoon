for _ in range(int(input())):
    s, p = input().split()
    s = s.replace(p, '-')
    print(len(s))