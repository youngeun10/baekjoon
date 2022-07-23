import sys

card = sys.stdin.readline().strip()
cnt = {'P': [], 'K': [], 'H': [], 'T': []}

for i in range(len(card)//3):
    n = card[(i*3):(i*3)+3]
    sign = card[i*3]
    
    if n in cnt[sign]:
        print("GRESKA")
        quit()
    else:
        cnt[sign].append(n)

print(13-len(cnt['P']), 13-len(cnt['K']), 13-len(cnt['H']), 13-len(cnt['T']))