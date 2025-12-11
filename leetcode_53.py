#Solution 1
class Solution(object):
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = float('-inf')

        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum
    
#Solution 2
class Solution(object):
    def max_sub(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum+nums[i])
            max_sum = max(current_sum, max_sum)
        return max_sum
    
sol = Solution()
print(sol.maxSubArray(nums = [5,4,-1,7,8]))