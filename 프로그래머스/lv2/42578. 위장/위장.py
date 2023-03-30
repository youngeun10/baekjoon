def solution(clothes):
    closet = {}
    for v, c in clothes:
        if c in closet:
            closet[c] += 1
        else:
            closet[c] = 1
    res = 1
    for c in closet.keys():
        res *= (closet[c]+1)

    return res - 1