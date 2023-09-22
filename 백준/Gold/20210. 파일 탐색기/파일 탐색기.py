from functools import cmp_to_key


def to_list(word):
    li = list(word)
    i = 0
    while i < len(li):
        if li[i].isdigit():
            end = i
            while end < len(li) and li[end].isdigit():
                end += 1
            li[i:end] = [''.join(li[i:end])]
            i = end - 1
        i += 1
    return li


def diff(w1, w2):
    w1 = to_list(w1)
    w2 = to_list(w2)
    i = 0
    while i < min(len(w1), len(w2)):
        if w1[i] == w2[i]:
            i += 1
            continue
        # 숫자와 문자 비교
        if w1[i].isdigit() and w2[i].isalpha():
            return -1
        elif w1[i].isalpha() and w2[i].isdigit():
            return 1
        # 문자와 문자 비교
        elif w1[i].isalpha() and w2[i].isalpha():
            if w1[i].lower() == w2[i].lower():
                return -1 if w1[i] < w2[i] else 1
            return -1 if w1[i].lower() < w2[i].lower() else 1
        # 숫자와 숫자 비교
        elif w1[i].isdigit() and w2[i].isdigit():
            if int(w1[i]) == int(w2[i]):
                z1 = len(w1[i])-len(w1[i].lstrip('0'))
                z2 = len(w2[i])-len(w2[i].lstrip('0'))
                return -1 if z1 < z2 else 1
            else:
                return -1 if int(w1[i]) < int(w2[i]) else 1
        i += 1
    return -1 if len(w1) < len(w2) else 1

# answer
print(*sorted([input() for _ in range(int(input()))], key=cmp_to_key(diff)), sep='\n')