class Solution:
    def combine(self, n: int, k: int):
        curcomb, comb = [], []

        def dfs(i, curcomb, comb):
            if i==n+1:
                return 
            if len(curcomb)==k:
                comb.append(curcomb.copy())
                return
            
            curcomb.append(i)
            dfs(i+1, curcomb, comb)
            curcomb.pop()
            dfs(i+1, curcomb, comb)

        dfs(1, curcomb, comb)
        return comb
    
n=4
k=2
obj=Solution()
print(obj.combine(n,k))