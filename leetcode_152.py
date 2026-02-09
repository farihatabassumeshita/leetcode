#Solution 1
class Solution(object):
    def maxProduct(self, nums):
        positive_result = nums[0]
        negative_result = nums[0]
        max_product = nums[0]
        for num in nums[1::]:
            if num<0:
                positive_result, negative_result = negative_result, positive_result

            positive_result = max(num, positive_result*num)
            negative_result = min(num, negative_result*num)
            max_product = max(max_product, positive_result)
        return max_product
        
#Solution 2
class Solution(object):
    def maxProduct(self, nums):
        curr_max = curr_min = result = nums[0]
        for n in nums[1::]:
            temp = curr_max
            curr_max = max(n, n*curr_max, n*curr_min)
            curr_min = min(n, n*temp, n*curr_min)
            result = max(result, curr_max)
        return result
    
sol = Solution()
print(sol.maxProduct(nums = [2,3,-2,4]))