import heapq
class Median:
    def __init__(self):
        self.small, self.large = [], []

    def insert(self, n):
        heapq.heappush(self.small, -1 * n)
        if self.small and self.large and ((self.small[0] * -1 ) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # balancing the length of heaps
        if len(self.small) > len(self.large):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small):
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)


    def getmedian(self):
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            return self.large[0]
        
        else:
            return ((self.small[0] * -1)  + self.large[0])/2