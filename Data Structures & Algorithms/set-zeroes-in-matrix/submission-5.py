# the follwoig solution is using the constatnt space

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        # check for the first column
        first_col_zero = False
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # store the markers in the first row and col
        for i in range(rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # start from last element so that we do not destroy the markers
        for i in range(rows-1,-1,-1):
            for j in range(cols -1,0,-1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
            if first_col_zero:
                matrix[i][0] = 0
        
        