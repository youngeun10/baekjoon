def multiple(m, c):
    result = 0
    for i in m:
        result += int(i)

    if result < 10:
        print(c, 'YES', sep='\n') if result % 3 == 0 else print(c, 'NO', sep='\n')
    else:
        multiple(str(result), c+1)

n = input()
if int(n) < 10:
    print(0, 'YES', sep='\n') if int(n) % 3 == 0 else print(0, 'NO', sep='\n')
else:
    multiple(n, 1)