import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        min_heap = []
        lenght = len(matrix)
        for r in range(min(lenght,k)):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))
        while k>0:
            val, r, col = heapq.heappop(min_heap)
            if col + 1 < lenght:
                heapq.heappush(min_heap,(matrix[r][col+1], r, col+1))
            k -= 1
        return val

solc = Solution()
print(solc.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))