class Solution(object):
    def findNumberofLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:

                    #case 1: Found Longer LIS
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] +1
                        count[i] = count[j] #update count

                    #case 2: Found another LIS of same length
                    elif dp[j]+1 == dp[i]:
                        count[i] += count[j]
        max_len = max(dp)
        # ans = 0
        # for i in range(n):
        #     if dp[i] == max_len:
        #         ans += count[i]

        return sum(count[i] for i in range(n) if dp[i] == max_len)
    
sol = Solution()
print(sol.findNumberofLIS(nums = [1,3,5,4,7]))