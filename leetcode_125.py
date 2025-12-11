class Solution(object):
    def isPalindrome(self, s):
        letter = ''.join(ch.lower() for ch in s if ch.isalpha())
        return letter == letter[::-1]


sol = Solution()
print(sol.isPalindrome(s = "race a car"))