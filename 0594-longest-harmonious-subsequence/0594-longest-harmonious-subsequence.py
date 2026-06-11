class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        ans=0
        for i in range(len(nums)):
            while nums[i]-nums[left]>1:
                left+=1
            if nums[i]-nums[left]==1:
                ans=max(ans,i-left+1)
        return ans
