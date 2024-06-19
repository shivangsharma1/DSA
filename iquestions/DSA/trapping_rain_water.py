class Solution:
    def trap(self, height):
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)

        #calculating left max array
        for i in range(len(height)):
            if i == 0: 
                leftmax[i] = 0
            else:
                leftmax[i] = max(leftmax[i-1], height[i-1])
        print("leftmax", leftmax)
        #calcualting right max array

        for j in range(len(height)-1, -1,-1):
            if j == len(height)-1:
                rightmax[j] == 0
            else:
                rightmax[j] = max(height[j+1], rightmax[j+1])
        print("rightmax", rightmax)
        water = 0

        for i in range(len(height)):
            temp = min(leftmax[i], rightmax[i]) - height[i]
            if temp >0:
                water+=temp


        return water


obj = Solution()
obj.trap([0,1,0,2,1,0,1,3,2,1,2,1])