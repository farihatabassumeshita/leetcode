class Solution(object):
    def minCost_Bottomup(self, cost):
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        for i in range (2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[n-1], dp[n-2])
    
    def minCost_Spaceoptimize(self, cost):
        prev = cost[0]
        curr = cost[1]
        for i in range(2,len(cost)):
            prev, curr = curr, min(prev,curr)+cost[i]
        return min(curr,prev)
    
sol = Solution()
print(sol.minCost_Bottomup(cost=[1,100,1,1,1,100,1,1,100,1]))
print(sol.minCost_Spaceoptimize(cost=[1,100,1,1,1,100,1,1,100,1]))