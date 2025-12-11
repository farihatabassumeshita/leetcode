class Solution(object):
    def maxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        maximum_sum = window_sum
        for num in range(k,len(nums)):
            window_sum += nums[num] - nums[num - k]
            maximum_sum = max(window_sum, maximum_sum)
        return float(maximum_sum)/k
    
sol = Solution()
print(sol.maxAverage(nums = [1,12,-5,-6,50,3], k = 4))

