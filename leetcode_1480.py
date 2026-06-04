class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
    
sol = Solution()
print(sol.runningSum(nums=[1,2,3,4]))