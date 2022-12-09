cnt = 1
string = input()
for i in range(1, len(string)):
    if string[i] != string[i-1]:
        cnt += 1
print(cnt//2)