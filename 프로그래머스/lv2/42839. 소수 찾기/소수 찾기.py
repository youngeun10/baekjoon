from itertools import permutations
import math

def arrToInt(v):
    tmp = ''
    for i in v:
        tmp += i

    return int(tmp)

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    numArr = list(numbers)
    midResult = []
    answer = 0
    result = []

    for i in range(1, len(numArr)+1):
        midResult += permutations(numArr, i)
    midResult = set(midResult)
    
    for m in midResult:
        t = arrToInt(m)
        if t > 1 and t not in result:
            result.append(t)

    for r in result:
        if is_prime_number(r):
            answer += 1

    return answer