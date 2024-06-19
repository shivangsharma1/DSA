
def productExceptSelf(nums):
        leftmul, rightmul = [0]*len(nums), [0]*len(nums)
        res = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                leftmul[i] = nums[i]
            else:
                leftmul[i] = nums[i] * leftmul[i-1]

        for j in range(len(nums)-1, -1, -1):
            if j == len(nums)-1:
                rightmul[j] = nums[j]
            else:

                rightmul[j] = nums[j] * rightmul[j+1]
        
        
        for ele in range(len(res)):
            print("ele", ele)
            if ele == 0:
                res[ele] = rightmul[ele]
            elif ele == len(nums)-1:
                res[ele] = leftmul[ele]

            else:
                res[ele] = leftmul[ele-1] * rightmul[ele+1]




productExceptSelf([1,2,3,4])




