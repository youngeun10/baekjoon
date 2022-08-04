s = input()
result = []
for i in range(1, len(s)+1):
    c = 0
    for j in range(0, len(s)):
        result.append(s[j:j+i])
result = set(result)
print(len(result))