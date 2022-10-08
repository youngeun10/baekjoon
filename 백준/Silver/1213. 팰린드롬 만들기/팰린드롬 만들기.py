from sys import stdin

arr = stdin.readline().rstrip()
arr_cnt = [0 for _ in range(26)]

for a in arr:
    arr_cnt[ord(a)-65] += 1

odd = 0
odd_alphabet = ''
alphabet = ''

for i in range(26):
    if arr_cnt[i] % 2 == 1:
        odd += 1
        odd_alphabet += chr(i+65)
    alphabet += chr(i+65)*(arr_cnt[i]//2)

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(alphabet + odd_alphabet + alphabet[::-1])