class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) -1
        while left<right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left+1 , right+1]
            elif two_sum < target:
                left += 1
            else:
                right -= 1
                
    
sol = Solution()
print(sol.twoSum(numbers = [2,7,11,15], target = 9))