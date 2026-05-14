class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag=True
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    flag=False
                    return [i,j]
                    break
            if flag==False:
                break