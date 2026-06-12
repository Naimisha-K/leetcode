class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_row=[]
        for row in matrix:
            min_row.append(min(row))
        rows=len(matrix)
        cols=len(matrix[0])
        l=[]
        for j in range(0,cols):
            col=[]
            for i in range(0,rows):
                col.append(matrix[i][j])
            if max(col) in min_row:
                l.append(max(col))
        return l