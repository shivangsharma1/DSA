class Solution:
    def min_Swaps(self, nums):
        N = len(nums)
        total_ones = nums.count(1)
        print(total_ones)
        l = 0
        window_ones = max_window_ones = 0
        for r in range(2*N):
            b = r%N
            a = nums[r%N]
            if a:
                window_ones+=1
            if r - l + 1>total_ones:
                window_ones -=nums[l%N]
                l += 1
                
            max_window_ones = max(max_window_ones, window_ones)

        return total_ones - max_window_ones
    

obj = Solution()
example = [0, 1, 0, 1, 1, 0, 0]
print(obj.min_Swaps(example))

