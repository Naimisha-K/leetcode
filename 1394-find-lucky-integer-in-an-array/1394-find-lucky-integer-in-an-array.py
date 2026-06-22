class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n=-1
        lar=arr[0]
        for i in arr:
            if arr.count(i)==i:
                n=max(n,i)
        return n 