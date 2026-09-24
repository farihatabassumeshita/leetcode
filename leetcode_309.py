class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0,0] for _ in range(n+2)]

        for i in range(n-1, -1, -1):
            #Buy state
            dp[i][0] = max(
                dp[i+1][0], #skip
                dp[i+1][1] - prices[i] #buy
            )

            #we are holding a stock
            dp[i][1] = max(
                dp[i+1][1], #skip
                dp[i+2][0] + prices[i] #sell+cooldown
            )
        return dp[0][0]

sol = Solution()
print(sol.maxProfit(prices=[1,3,4,0,4]))
