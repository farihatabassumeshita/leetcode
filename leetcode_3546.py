class Solution(object):
    def canPartitionGrid(self, grid):
        store_sum = total_sum = 0
        total_sum = sum(sum(m) for m in grid)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        #Horizontal Cut
        for i in range(len(grid)):
            store_sum += sum(grid[i])
            if store_sum == target:
                return True
        #Vertical Cut
            #First compute column sum
        col_sum = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid)):
                col_sum[j] += grid[i][j]
            #Prefix Sum on colums
        for p in range(col_sum):
            store_sum += col_sum[p]
            if store_sum == target:
                return True
        return False
    
sol = Solution()
print(sol.canPartitionGrid(grid = [[1,2,3],[3,2,1]]))