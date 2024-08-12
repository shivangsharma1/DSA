def subsetwithduplicate(nums):
    nums.sort()
    subset, curset = [], []
    helper(0, curset, subset, nums)
    return subset


def helper(i, curset, subset, nums):
    if i == len(nums):
        subset.append(curset.copy())
        return
    
    curset.append(nums[i])
    helper(i+1, curset, subset, nums)
    curset.pop()

    while i+1<len(nums) and nums[i] == nums[i+1]:
        i+=1

    helper(i+1, curset, subset, nums)