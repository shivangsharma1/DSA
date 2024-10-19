import heapq
class Solution:
    def get_median(self, k):
        if k%2 == 0:
            ele1, ind1 = self.maxheap[0]
            ele2, ind2 = self.minheap[0]

            fin = (-ele1 + ele2)/2
            return fin
            
        else:
            if len(self.minheap) > len(self.maxheap):
                fin, index = self.minheap[0]
                return fin
            else:
                fin, index = self.maxheap[0]
                return -fin
    
    def rebalance(self):

        while len(self.maxheap) > len(self.minheap)+1:
            ele, index = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, (-ele, index))
        
        while len(self.minheap) > len(self.maxheap)+1:
            ele, index = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, (-ele, index))
    
    def addnum(self, num, index):
        heapq.heappush(self.maxheap, (-num, index))
        if self.minheap and self.maxheap and -self.maxheap[0][0] > self.minheap[0][0]:
            ele, index = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, (-ele, index))

        self.rebalance()
        
    def remove(self, heap):
        while heap and heap[0][1] in self.hashset:
            heapq.heappop(heap)


    def medianSlidingWindow(self, nums, k):
        self.maxheap = [] #maxheap
        self.minheap = [] #minheap
        self.hashset = set()
        self.res = []
        left = 0
        for index, right in enumerate(nums):
            self.addnum(right, index)

            if index-left+1 == k:
                med = self.get_median(k)
                self.res.append(med)
                self.hashset.add(left)
                self.remove(self.minheap)
                self.remove(self.maxheap)
                self.rebalance()
                left+=1

        return self.res



nums = [1,3,-1,-3,5,3,6,7]
k = 3

obj = Solution()
print(obj.medianSlidingWindow(nums, k))