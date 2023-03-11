def solution(record):
    user = {}
    tmp = []
    answer = []
    for u in record:
        t = u.split()
        if t[0] == "Enter":
            user[t[1]] = t[2]
            tmp.append(t[1]+"i")
        elif t[0] == "Leave":
            tmp.append(t[1]+"o")
        else:
            user[t[1]] = t[2]

    for t in tmp:
        if t[-1] == "i":
            answer.append(str(user[t[:-1]])+"님이 들어왔습니다.")
        else:
            answer.append(str(user[t[:-1]]) + "님이 나갔습니다.")
    
    return answer