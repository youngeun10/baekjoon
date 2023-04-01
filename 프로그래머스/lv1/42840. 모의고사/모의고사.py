def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    sc = [0, 0, 0]

    for idx, s in enumerate(answers):
        if answers[idx] == s1[idx % len(s1)]:
            sc[0] += 1
        if answers[idx] == s2[idx % len(s2)]:
            sc[1] += 1
        if answers[idx] == s3[idx % len(s3)]:
            sc[2] += 1

    for idx, v in enumerate(sc):
        if sc[idx] == max(sc):
            answer.append(idx+1)
    return answer