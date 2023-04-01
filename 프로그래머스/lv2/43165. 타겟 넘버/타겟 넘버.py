def solution(numbers, target):
    idx = curr = 0

    def dfs(nums, target, curr, idx):
        # 결과 비교는 마지막에 인덱스가 끝까지 갔을 때 합니다
        if idx == len(nums):
            return 1 if curr == target else 0

        # idx를 한칸 움직여주고 curr에 이번 값을 더하거나 뺍니다
        return dfs(nums, target, curr + nums[idx], idx + 1) \
                + dfs(nums, target, curr - nums[idx], idx + 1)

    answer = dfs(numbers, target, idx, curr)
    return answer