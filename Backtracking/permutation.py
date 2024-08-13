def permutation(nums):
    return helper(0, nums)


def helper(i, nums):
    if i==len(nums):
        return [[]]
    
    res_perms = []
    perms = helper(i+1, nums)
    
    for p in perms:
        for j in range(len(p)+1):
            pcopy = p.copy()
            pcopy.insert(j, nums[i])
            res_perms.append(pcopy)

    return res_perms