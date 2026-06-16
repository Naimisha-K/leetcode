class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i, j in enumerate(nums):
            c=target-j
            if c in d:
                return [d[c],i]
            d[j]=i