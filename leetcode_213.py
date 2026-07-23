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
    
    def houserobber_BottomUP(self, nums):
        n = len(nums)
        if n <= 1:
            return nums[0]
        def rob_linear(arr):
            n = len(arr)
            if n <= 1:
                return arr[0]
            dp = [0] * n
            dp[0], dp[1] = arr[0], max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2]+arr[i])
            return dp[-1]
        return max(
            rob_linear(nums[1:]),
            rob_linear(nums[:-1])
        )

sol = Solution()     
print(sol.houserobber_BottomUP(nums = [1,2,3,1]))