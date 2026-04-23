class Solution(object):
    def trap(self, height):
        left, right, left_max, right_max, trap_count = 0, len(height)-1, 0, 0, 0
        while left<right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trap_count += left_max - height[left]
                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trap_count += right_max - height[right]
                right -= 1
        return trap_count
    
sol = Solution()
print(sol.trap(height = [4,2,0,3,2,5]))

