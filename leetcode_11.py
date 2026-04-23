class Solution(object):
    def maxArea(self, height):
        left, right, max_area = 0, len(height) - 1, 0
        while left<right:
            width = right - left
            height_area = min(height[left], height[right])
            area = width * height_area
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
sol = Solution()
print(sol.maxArea(height = [1,1]))
            

