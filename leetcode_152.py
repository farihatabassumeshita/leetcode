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
        
    
sol = Solution()
print(sol.maxProduct(nums = [2,3,-2,4]))