class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for index, num in enumerate(nums):
            if num in hashset:
                return index, hashset[num]
            else:
                subtract = target - num
                hashset[subtract] = index