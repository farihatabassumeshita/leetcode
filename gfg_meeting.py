class Solution(object):
    def nMeeting(self, start, end):
        meeting = [(start[i], end[i], i+1) for i in range(len(start))]
        meeting.sort(key=lambda x:x[1])
        return meeting
sol = Solution()
print(sol.nMeeting(start = [1, 3, 0, 5, 8, 5], end =  [2, 4, 6, 7, 9, 9]))