class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        max_left, max_right = 0, 0

        left, right = 0, len(height)-1
        while left<right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            
            if max_left <= max_right:
                temp = max_left - height[left]
                left+=1
            else:
                temp = max_right - height[right]
                right-=1

            if temp>0:
                total_water+=temp

        return total_water
