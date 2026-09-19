class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # the key here is to do a transpose first that is converting the rows to columns and columns to rows
        # once done then do a horizontal reflection

        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        

        # Horizontal Reflection
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]