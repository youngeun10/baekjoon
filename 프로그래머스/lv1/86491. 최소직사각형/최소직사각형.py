def solution(sizes):
    tmp = []
    for f, s in sizes:
        if f > s:
            tmp.append((s, f))
        else:
            tmp.append((f, s))

    mw = 0
    md = 0
    for w, d in tmp:
        mw = max(mw, w)
        md = max(md, d)
    answer = mw * md
    return answer