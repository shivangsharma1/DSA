class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        count = 0
        for num in nums:
            hashmap[num] = 1+hashmap.get(num, 0)

        for i in hashmap.values():
            if i >1:
                count+=1
        return True if count>0 else False