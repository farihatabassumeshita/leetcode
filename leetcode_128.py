class Solution(object):
    def longestConsecutive(self, nums):
        numset = set(nums)
        longest = 0
        for num in numset:
            if (num-1) not in numset:
                length = 0
                while (num + length) in numset:
                    length += 1
                longest = max(longest, length)
        return longest
    
sol = Solution()
print(sol.longestConsecutive(nums = [100,4,200,1,3,2,5]))