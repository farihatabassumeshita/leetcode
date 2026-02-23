class Solution(object):
    def insert(self, intervals, newInterval):
        merge = []
        i=0
        #Add all intervals before nreInntervals
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merge.append(intervals[i])
            i+=1

        #merge overlaping intervals
        while i<len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        merge.append(newInterval)

        #After overlaping
        while i<len(intervals):
            merge.append(intervals[i])
            i+=1
        return merge
sol = Solution()
print(sol.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
