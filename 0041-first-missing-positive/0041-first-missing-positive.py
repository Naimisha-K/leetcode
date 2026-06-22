class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        k=1
        for i in range(len(s)):
            if k not in s:
                return k
                break
            k+=1
        return k