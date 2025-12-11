class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], index]
            seen[num] = index

sol = Solution()
print(sol.twoSum(nums = [2,7,11,15], target = 9))