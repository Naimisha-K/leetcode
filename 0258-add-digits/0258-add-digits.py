class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        while True:
            while num>0:
                d=num%10
                s=s+d
                num=num//10
            if s>9:
                num=s
                s=0
            else: 
                return s   