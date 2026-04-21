class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
    
sol = Solution()
print(sol.removeDuplicates(nums = [1,1,2]))
