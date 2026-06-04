class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
    
sol = Solution()
print(sol.containsDuplicate(nums = [1, 2, 3, 3]))
        
