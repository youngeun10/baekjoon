import sys
yin = sys.stdin.readline

def wordCombi(idx, arr):
    global wordCombiArr

    if len(arr) == K - 5:
        wordCombiArr.append(arr)
        return arr

    for i in range(idx+1, len(word)):
        if not visited[i]:
            visited[i] = True
            wordCombi(i, arr + [word[i]])
            visited[i] = False

N, K = map(int, yin().split())
alph = {'b': 0, 'd': 1, 'e':2, 'f': 3, 'g': 4, 'h': 5, 'j': 6, 'k': 7, 'l': 8, 'm': 9, 'o': 10
    , 'p': 11, 'q': 12, 'r': 13, 's': 14, 'u': 15, 'v': 16, 'w': 17, 'x': 18, 'y': 19, 'z': 20}
wordArr = []            # antic를 제외한 것들이 알파벳의 위치 저장
word = []               # 현재 antic를 제외한 알파벳의 위치 저장 -> 나중에 조합 만들기에 사용

# 1
for _ in range(N):
    tmpArr = list(yin().rstrip())
    tmp = [0] * 21
    for s in tmpArr[4:len(tmpArr)-4]:
        if s not in "antic":
            tmp[alph[s]] = 1
            if alph[s] not in word:
                word.append(alph[s])
    wordArr.append(tmp)

if K < 5:
    print(0)
    exit()

# 2
visited = [False] * len(word)
wordCombiArr = []
wordCombi(-1, [])

if wordCombiArr == []:
    print(N)
    exit()
# 3
result = 0
for wc in wordCombiArr:
    midResult = 0
    for wa in wordArr:
        tmp = wa[:]
        for w in wc:
            tmp[w] = 0
        if sum(tmp) == 0:
            midResult += 1
    result = max(midResult, result)
print(result)