class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        path = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            if r < 0 or c < 0:
                return False
            if r >= rows or c >= columns:
                return False
            if word[i] != board[r][c]:
                return False
            if (r,c) in path:
                return False
            
            path.add((r,c))
            ans = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            path.remove((r,c))
            return ans
        
        for r in range(rows):
            for c in range(columns):
                if dfs(r,c,0): return True
        return False