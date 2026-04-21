class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], index]
            seen[num] = index
    #Two pointer solution
    def twoSumtwopointer(self, nums, target):
        arr = list(enumerate(nums)) #(index,value)
        arr.sort(key=lambda x: x[1])

        left, right = 0, len(nums)-1
        while left < right:
            s = arr[left][1] + arr[right][1]
            if s == target:
                return [arr[left][0], arr[right][0]]
            elif s < target:
                left += 1
            else:
                right -= 1
        return []

sol = Solution()
print(sol.twoSumtwopointer(nums = [2,7,11,15], target = 9))