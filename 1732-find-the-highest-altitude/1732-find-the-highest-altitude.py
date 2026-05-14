class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x=0
        al=[0]
        for i in gain:
            x=x+i
            al.append(x)
        return max(al)