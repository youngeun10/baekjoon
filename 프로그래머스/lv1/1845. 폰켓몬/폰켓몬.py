def solution(nums):
    tmp = {}

    for i in nums:
        if i not in tmp:
            tmp[i] = 1
        else:
            tmp[i] += 1

    answer = len(tmp.keys()) if len(nums) // 2 > len(tmp.keys()) else len(nums) // 2

    return answer
