class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        # start with rows:
        for i in range(rows):
            seen = set()
            for j in range(cols):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                if board[i][j] != ".":
                    seen.add(board[i][j])

        # check cols:
        for i in range(cols):
            seen = set()
            for j in range(rows):
                if board[j][i] in seen and board[j][i] != ".":
                    return False
                if board[j][i] != ".":
                    seen.add(board[j][i])

        
        # check for the boxes:
        start = [(0,0),(0,3),(0,6),
                 (3,0),(3,3),(3,6),
                 (6,0),(6,3),(6,6)]
        
        for i,j in start:
            seen = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    item = board[row][col]
                    if item in seen:
                        return False
                    if item!= ".":
                        seen.add(item)
        
        return True