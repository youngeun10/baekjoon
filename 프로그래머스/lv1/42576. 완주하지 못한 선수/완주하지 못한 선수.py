def solution(participant, completion):
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