class Solution(object):
    def isPalindrpme(self, x):
        s = str(x)
        return s == s[::-1]
    
    
sol = Solution()
print(sol.isPalindrpme(x = -121))