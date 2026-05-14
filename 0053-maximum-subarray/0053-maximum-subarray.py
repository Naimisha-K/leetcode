class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        msum=float('-inf')
        csum=0
        for i in range(n):
            csum=csum+nums[i]
            if msum<csum:
                msum=csum
            if csum<0:
                csum=0
        return msum