def solution(participant, completion):
    p = set(participant)
    c = set(completion)

    if len(p) - len(c) == 1:
        for i in c:
            p.remove(i)
        answer = list(p)[0]
        return answer
    else:
        p = {}
        for i in participant:
            if i not in p:
                p[i] = 1
            else:
                p[i] += 1
        for i in completion:
            p[i] -= 1
        answer = [k for k, v in p.items() if v == 1]

    return answer[0]