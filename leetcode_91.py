class Solution(object):
    def numDecodings(self, s):
        length = len(s)
        dp = [0] * (length+1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        for i in range(2,length+1):
            #Take one digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            #Take two digit
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        return dp[length]

sol = Solution()
print(sol.numDecodings(s="12")) 
            
            