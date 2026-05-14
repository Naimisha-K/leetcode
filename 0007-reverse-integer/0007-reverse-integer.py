class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        c=0
        if x<0:
            x=-x
            c=1
        while x>0:
            d=x%10
            rev=(rev*10)+d
            x//=10
        if c==1:
            rev=-rev
        if rev<-2**31 or rev>2**31-1:
            return 0
        return rev

        