class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=set()
        c=set()
        box=set()
        for i in range(9):
            for j in range(9):
                x=board[i][j]
                if x==".":
                    continue
                if (i,x) in r:
                    return False
                if (j,x) in c:
                    return False
                if (i//3,j//3,x) in box:
                    return False
                box.add((i//3,j//3,x))
                r.add((i,x))
                c.add((j,x))
        return True