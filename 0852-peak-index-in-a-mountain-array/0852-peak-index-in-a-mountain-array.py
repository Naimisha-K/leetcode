class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        m=arr[0]
        l=0
        for i in range(len(arr)):
            if m<arr[i]:
                m=arr[i]
                l=i
        return l

         