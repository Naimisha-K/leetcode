class Solution:
    def replaceDigits(self, s: str) -> str:
        n=len(s)
        r=""
        for i in range(n):
            if i%2==0:
                r+=s[i]
            else:
                r+=chr(ord(s[i-1])+int(s[i]))
        return r