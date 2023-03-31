import collections
def solution(s):
    stack = collections.deque([])
    for t in s:
        if t == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    answer = False if len(stack) > 0 else True
    return answer