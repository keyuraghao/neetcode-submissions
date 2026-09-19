class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        ROW = [0] * rows
        COL = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    ROW[i] = 1
                    COL[j] = 1
        
        for i in range(rows):
            for j in range(cols):
                if ROW[i] == 1:
                    matrix[i][j] = 0
                if COL[j] == 1:
                    matrix[i][j] = 0