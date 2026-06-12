class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)-len(s1)+1):
            a=s2[i:i+len(s1)]
            if sorted(a)==sorted(s1):
                return True
                break
        else:
            return False