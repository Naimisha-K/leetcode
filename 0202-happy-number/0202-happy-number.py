class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1 and n!=4:
            s=0
            while n>0: 
                d=n%10
                s=s+d**2
                n=n//10
            n=s
        if n==1:
            return True
        else:
            return False
        