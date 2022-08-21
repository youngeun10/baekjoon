s = 1

while True:
    name = {}
    earring = {}
    
    std = int(input())
    if std == 0:
        quit()
    for i in range(std):
        name[str(i+1)] = input()
        earring[str(i+1)] = ['A', 'B']

    for i in range((2*std)-1):
        n, p = input().split()
        earring[n].remove(p)
        if len(earring[n]) == 0:
            del name[n]

    print(s, *name.values())
    s += 1