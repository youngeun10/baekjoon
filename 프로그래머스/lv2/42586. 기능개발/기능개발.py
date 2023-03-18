def solution(progresses, speeds):
    answer = []
    tmp = [(100 - progresses[0]) // speeds[0] if (100 - progresses[0]) % speeds[0] == 0 else ((100 - progresses[0]) // speeds[0]) + 1]

    for i in range(1, len(progresses)):
        t = (100 - progresses[i]) // speeds[i] if (100 - progresses[i]) % speeds[i] == 0 else ((100 - progresses[i]) // speeds[i]) + 1
        tmp.append(tmp[-1] if t < tmp[-1] else t)

    tmp.append(0)
    c = tmp[0]
    cnt = 1

    for i in range(1, len(tmp)):
        if c != tmp[i]:
            answer.append(cnt)
            cnt = 1
            c = tmp[i]
        else:
            cnt += 1

    return answer