class Solution(object):
    def jump(self, nums):
        jumps = 0
        currFarther = 0
        currEnd = 0
        for i in range(len(nums)-1):
            currFarther = max(currFarther, i+nums[i])
            if i == currEnd:
                currEnd = currFarther
                jumps += 1
        return jumps