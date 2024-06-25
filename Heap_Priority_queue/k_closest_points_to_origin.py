import heapq

class Solution:
    def dist(self, point):
        return ((point[0])**2 + (point[1])**2) ** 0.5
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        arr = [[self.dist(point), point[0], point[1]] for point in points] 
        heapq.heapify(arr)

        res = []
        while k:
            dist, x, y = heapq.heappop(arr)
            res.append([x, y])
            k-=1

        return res