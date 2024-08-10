class Solution:
    def dailyTemperatures(self, temperatures):
        l=[0]*len(temperatures)
        stack=[]
        for i,val in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<val:
                j=stack.pop()
                l[j]=i-j
                
            stack.append(i)
        return l
obj = Solution()
examples = [73,74,75,71,69,72,76,73]
print(obj.dailyTemperatures(examples))