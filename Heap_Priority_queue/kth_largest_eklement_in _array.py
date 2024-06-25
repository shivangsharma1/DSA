import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-n for n in nums]
        heapq.heapify(arr)
        n = k-1
        while n:
            heapq.heappop(arr)
            n-=1

        return -heapq.heappop(arr)
        