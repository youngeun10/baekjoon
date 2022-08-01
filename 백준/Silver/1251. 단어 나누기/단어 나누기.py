from sys import stdin
word = list(stdin.readline().rstrip())
wordArr = []
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
       a = word[0:i]
       b = word[i:j]
       c = word[j:]

       a.reverse()
       b.reverse()
       c.reverse()

       wordArr.append(a+b+c)

wordArr.sort()
print(*wordArr[0], sep='')