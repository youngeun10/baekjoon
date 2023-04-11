import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville)*2))
        except:
            return -1
        answer += 1

    return answer