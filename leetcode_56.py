class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0]) 
        merge = [intervals[0]]  
        prev_end = intervals[0][1]   
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if curr_start > prev_end:
                merge.append(intervals[i])
                prev_end = curr_end
            else:
                prev_end = max(curr_end, prev_end)
                merge[-1][1] = prev_end
        return merge
                
sol = Solution()
print(sol.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))