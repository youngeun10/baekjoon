def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    s1 *= (len(answers) // 5)+1
    s2 *= (len(answers) // 8)+1
    s3 *= (len(answers) // 10)+1

    sc = [0, 0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == s1[i]:
            sc[1] += 1
        if answers[i] == s2[i]:
            sc[2] += 1
        if answers[i] == s3[i]:
            sc[3] += 1

    for i in range(1, len(sc)):
        if max(sc) == sc[i]:
            answer.append(i)
    return answer