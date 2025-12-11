import heapq
class MedianFinder(object):
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        heapq.heappush(self.max_heap, -num)

        if self.min_heap and -self.max_heap[0]>self.min_heap:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        if len(self.max_heap) > len(self.min_heap):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-val)

    def findMedian(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0])/2.0
        
sol = MedianFinder()
sol.addNum(41)
sol.addNum(35)
sol.addNum(62)
sol.addNum(4)
print(sol.findMedian())
