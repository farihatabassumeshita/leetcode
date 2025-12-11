class Solution(object):
    def maxProfit(self, prices):
        left = 0
        result = 0
        for right in range(1,len(prices)):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                if profit > 0:
                    result += profit
            left = right
        return result
    
Sol = Solution()
print(Sol.maxProfit(prices = [7,1,5,3,6,4]))
