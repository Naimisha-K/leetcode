class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avgs=sum(nums[:k])
        max_avg=avgs
        for i in range(k,len(nums)):
            avgs=avgs+nums[i]-nums[i-k]
            max_avg=max(max_avg,avgs)
        return max_avg/k