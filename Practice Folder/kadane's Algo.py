def max_sum_subarray(arr): #brute force
    maxsum = float('-inf')
    for i in range(len(arr)):
        cursum = 0
        for j in range(i, len(arr)):
            cursum+=arr[j]
            maxsum = max(maxsum, cursum)

    return maxsum

class Solution:
    def maxSubArray(self, nums) -> int: #kadanes' algo
        cursum, maxsum = 0, nums[0]
        for n in nums:
            cursum = max(cursum, 0)
            cursum+=n
            maxsum = max(cursum, maxsum)

        return maxsum



arr = [4, -1, 2, -7, 3, 4]
print(max_sum_subarray(arr))

