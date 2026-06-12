# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        k=0
        while n>0:
            while not isBadVersion(n+k):
                k+=n
            n//=2
        return k+1