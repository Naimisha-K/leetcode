class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums)>1:
                l=nums[:len(nums)//2]
                r=nums[len(nums)//2:]
                mergesort(l)
                mergesort(r)
                i=j=k=0
                while i<len(l) and j<len(r):
                    if l[i]<r[j]:
                        nums[k]=l[i]
                        i+=1
                        k+=1
                    else:
                        nums[k]=r[j]
                        j+=1
                        k+=1
                while i<len(l):
                    nums[k]=l[i]
                    i+=1
                    k+=1
                while j<len(r):
                    nums[k]=r[j]
                    j+=1
                    k+=1
        mergesort(nums)
        return nums