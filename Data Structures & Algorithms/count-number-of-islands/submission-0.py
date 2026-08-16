from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        if not grid :
            return 0

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                r,c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    if (r+dr) in range(ROWS) and (c+dc) in range(COLS) and grid[r+dr][c+dc] =="1" and (r+dr,c+dc) not in visited:
                        q.append((r+dr,c+dc))
                        visited.add((r+dr,c+dc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands