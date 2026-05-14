class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n=0
        for i in grid:
            for j in i:
                if j<0:
                    n=n+1
        return n