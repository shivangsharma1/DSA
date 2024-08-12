def subsetwithoutduplicate(nums):
    subsets, curset = [], []
    helper(0, curset, subsets, nums)
    return subsets


def helper(i, curset, subsets, nums):
    if i==len(nums):
        subsets.append(curset.copy())
        return
    
    curset.append(nums[i])
    helper(i+1, curset, subsets, nums)
    curset.pop()
    helper(i+1, curset, subsets, nums)