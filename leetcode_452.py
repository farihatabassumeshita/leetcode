class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])
        i = 0
        arrow = 1
        prev_end = points[0][1]
        for i in range(1, len(points)):
            curr_start, curr_end = points[i][0], points[i][1]
            if curr_start > prev_end:
                prev_end = curr_end
                arrow += 1
                i += 1
        return arrow
    
sol = Solution()
print(sol.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))