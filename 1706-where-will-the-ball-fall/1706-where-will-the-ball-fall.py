class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m= len(grid)
        n=len(grid[0])
        res = []
        for c in range(n):
            col = c
            for row in range(m):
                next_col = col + grid[row][col]
                if next_col < 0 or next_col >= n or grid[row][col] ^ grid[row][next_col]:
                    col = -1
                    break
                col = next_col
            res.append(col)
        return res