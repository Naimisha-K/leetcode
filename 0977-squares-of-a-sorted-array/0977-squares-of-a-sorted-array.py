class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[0]*len(nums)
        left=0
        right=len(nums)-1
        i=len(nums)-1
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                l[i]=nums[left]**2
                left+=1
            else:
                l[i]=nums[right]**2
                right-=1
            i-=1
        return l