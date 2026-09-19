class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        LEFT, RIGHT, UP, DOWN = 1,2,3,4
        ans = []
        i = j = 0
        rows = len(matrix)
        cols = len(matrix[0])

        left_wall = -1
        right_wall = cols
        up_wall = 0
        down_wall = rows

        direction = RIGHT

        while len(ans) != (rows*cols):
            if direction == RIGHT:
                while j < right_wall:
                    ans.append(matrix[i][j])
                    j += 1
                i += 1
                j -= 1
                right_wall -= 1
                direction = DOWN
            elif direction == DOWN:
                while i < down_wall:
                    ans.append(matrix[i][j])
                    i += 1
                i-=1
                j-=1
                down_wall -= 1
                direction = LEFT
            elif direction == LEFT:
                while j > left_wall:
                    ans.append(matrix[i][j])
                    j -= 1
                i -= 1
                j += 1
                left_wall += 1
                direction = UP
            else:
                while i > up_wall:
                    ans.append(matrix[i][j])
                    i -= 1
                i+=1
                j += 1
                up_wall += 1
                direction = RIGHT
        return ans
