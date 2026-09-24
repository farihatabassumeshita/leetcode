class Solution(object):
    def wallsandGates(self, grid):
        row, col = len(grid), len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c] == -1:
                return 
            distance = 0
            grid[r][c] = 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            distance += 1
            return distance

        for r in range(row):
            for c in range(col):
                if grid[r][c] == -1:
                    break
                elif grid[r][c] == 2147483647:
                    grid[r][c] = dfs(r,c)
        return grid