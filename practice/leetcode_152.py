class Solution(object):
    def maxProduct(self, nums):
        # current_sum_cal = current_sum = max_sum = nums[0]
        # for i in range(len(nums)):
        #     current_sum_cal = max(nums[i], (current_sum+nums[i]))
        #     current_sum = current_sum_cal
        #     max_sum = max(max_sum, current_sum)
        # return max_sum
        current_max = current_min = answer = nums[0]
        for num in nums[1::]:
            old_max = current_max
            old_min = current_min
            current_max = max(num, old_min * num, old_max * num)
            current_min = min(num, old_min * num, old_max * num)
            answer = max(answer, current_max)
        return answer

sol = Solution()
print(sol.maxProduct(nums=[2,3,-2,4]))

