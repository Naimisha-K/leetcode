class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_water=0
        while left<right:
            t=min(height[left],height[right])*(right-left)
            if t>max_water:
                max_water=t
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_water