# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def guessNum(l,h):
            diff=(h-l)
            g=diff//2 +l
            r=guess(g)
            if r==0:
                return g
            elif r==-1:
                return guessNum(l,g-1)
            elif r==1:
                return guessNum(g+1,h)
        return guessNum(1,n)