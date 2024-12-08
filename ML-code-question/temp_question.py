# n combinations from this list where n in the number of elements in the bigger list and each element in a given list can only be used once
# [[7, 4], [8, 5]]
# [[7,8], [7,5], [4,8], [4,5]]

class Solution:
    def return_combs(self, nums):
        curcomb, comb = [], []
        
        def dfs(i, curcomb):
            #base condition
            if len(curcomb) == len(nums):
                comb.append(curcomb.copy())
                return 

            if i == len(nums):
                return
            
            # for j in range(len(nums[i])):
            #     dfs(i+1, curcomb + [nums[i][j]])

            for ele in nums[i]:
                dfs(i+1, curcomb + [ele])
                
        dfs(0, curcomb)
        return comb
        


if __name__ ==  '__main__':
    obj = Solution()
    nums = [[7, 4, 3], [8, 5, 2]]
    print(obj.return_combs(nums))
