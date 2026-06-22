class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=0
        for i in range(len(nums)):
            if i>l:
                return False
            l=max(l,i+nums[i])
        return True