class Solution(object):
    def houserobber(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        def rob_line(arr):
            prev, curr = 0, 0
            for num in arr:
                prev, curr = curr, max(curr, prev+num)
            return curr
        
        #case 1: ignore last 
        case1 = rob_line(nums[:-1])
        #case 2: ignore first
        case2 = rob_line(nums[1:])
        return max(case1, case2)
        