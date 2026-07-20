import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_neg = [-stone for stone in stones]
        heapq.heapify(stones_neg)

        while len(stones_neg) > 1 :
            y = - heapq.heappop(stones_neg)
            x = - heapq.heappop(stones_neg)
            if x < y :
                heapq.heappush(stones_neg,x-y)
        if len(stones_neg) == 1 :
            return -stones_neg[0]
        else :
            return 0

        