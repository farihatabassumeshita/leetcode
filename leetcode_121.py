class Solution(object):
    def maxProfit(self, prices):
        left = 0
        result = 0
        for right in range(1,len(prices)):
            if prices[right] > prices[left]:
                result = max(result, prices[right] - prices[left])
            else:
                left = right
        return result
    
sol = Solution()
print(sol.maxProfit(prices = [7,1,5,3,6,4]))
