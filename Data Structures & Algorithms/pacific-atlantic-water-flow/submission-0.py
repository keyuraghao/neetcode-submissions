class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pac = set()
        atl = set()

        def dfs(row,col,visted_set,prev_heights):
            if row < 0 or col < 0:
                return
            if row >= ROWS or col >= COLS:
                return
            if heights[row][col] < prev_heights:
                return
            if (row,col) in visted_set:
                return
            visted_set.add((row,col))
            dfs(row+1,col,visted_set,heights[row][col])
            dfs(row-1,col,visted_set,heights[row][col])
            dfs(row,col+1,visted_set,heights[row][col])
            dfs(row,col-1,visted_set,heights[row][col])


        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        
        ans = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    ans.append([r,c])
        return ans