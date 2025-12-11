from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q = deque()
        max_array = []
        for i, num in enumerate(nums):
            if q and q[0] < i-k+1:
                q.popleft()
            while q and nums[q[-1]]<num:
                q.pop()
            q.append(i)
            if i>=k-1:
                max_array.append(nums[q[0]])
        return max_array
    
sol = Solution()
print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))

