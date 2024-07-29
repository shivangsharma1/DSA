

class Solution:
    def topKFrequent(self, nums, k):
        count_d = {}
        res = []
        l = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            count_d[i] = 1 + count_d.get(i, 0)
        
        for key, val in count_d.items():
            l[val].append(key)
        

        for i in range(len(l)-1, 0, -1):
            for ele in l[i]:
                res.append(ele)

                if len(res)>=k:
                    return res[:k]
                
obj = Solution()
inp = [1,1,1,2,2,3]
print(obj.topKFrequent(inp, 2))