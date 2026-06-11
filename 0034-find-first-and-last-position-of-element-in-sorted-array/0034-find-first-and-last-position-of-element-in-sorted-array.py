class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f=0
        l=len(nums)-1
        while f<=l and nums[f]!=target:
            f+=1
        while l>=f and nums[l]!=target:
            l-=1
        if f<=l:
            return [f,l]
        return [-1,-1]