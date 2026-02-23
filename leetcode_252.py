class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x:x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
    
sol = Solution()
print(sol.canAttendMeetings(intervals = [(0,30),(5,10),(15,20)]))