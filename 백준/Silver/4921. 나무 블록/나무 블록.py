def startEndChk(s):
    if s[0] == '1' and s[-1] == '2':
        return True
    return False

from sys import stdin
d = ["14", "15", "34", "35", "42", "43", "58", "62", "63", "78", "86", "87"]
cnt = 1

while True:
    text = stdin.readline().rstrip()
    if text == '0':
        break

    if startEndChk(text):
        chk = 0
        for i in range(len(text)-1):
            if str(text[i:(i+2)]) not in d:
                chk = 1
                break
        print(f"{cnt}. VALID") if chk == 0 else print(f"{cnt}. NOT")
    else:
        print(f"{cnt}. NOT")

    cnt += 1