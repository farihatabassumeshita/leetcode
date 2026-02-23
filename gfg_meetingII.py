import heapq
class Solution(object):
    def minMeetingRooms(self, start, end):
        meeting = [(start[i],end[i]) for i in range(len(start))]
        meeting.sort(key= lambda x: x[0])
        heap = []
        for s, e in meeting:
            if heap and s >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
        return len(heap)
    
sol = Solution()
print(sol.minMeetingRooms(start= [1, 10, 7], end= [4, 15, 10]))