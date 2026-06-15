class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        i=nums.index(m)
        for n in nums:
            if n!=m and m<2*n:
                return -1
        return i