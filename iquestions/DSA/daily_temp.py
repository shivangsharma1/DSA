class Solution:
    def dailyTemperatures(self, temperatures):
        res = []
        for i in range(len(temperatures)-1):
            cnt = i+1
            while temperatures[i]> temperatures[cnt]:
                cnt+=1
            res.append(cnt-i)
        print(res)
        res.append(0)
        return res
    


arr = [73,74,75,71,69,72,76,73]

obj = Solution()
obj.dailyTemperatures(arr)




class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i-stack_i

            stack.append([t, i])
        return res