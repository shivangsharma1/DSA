import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            y, x = heapq.heappop(stones), heapq.heappop(stones)
            if x == y:
                heapq.heappush(stones, 0)
            else:
                heapq.heappush(stones, y-x)

        return abs(stones[0])