class Solution(object):
    def island(self, grid):
        count = 0
        row, col = len(grid), len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=row or j>=col or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count +=1
        return count

sol = Solution()
print(sol.island(grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]))