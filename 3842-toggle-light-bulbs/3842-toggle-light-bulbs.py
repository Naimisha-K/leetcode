class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        res=[]
        for i in bulbs:
            if i not in res:
                res.append(i)
                res.sort()
            else:
                res.remove(i)
        return res