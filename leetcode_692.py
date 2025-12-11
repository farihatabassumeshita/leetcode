import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        min_heap = []
        count = Counter(words)
        for word, freq in count.items():
            heapq.heappush(min_heap, (-freq, word))
        return [heapq.heappop(min_heap)[1] for _ in range(k)]
    

sol = Solution()
print(sol.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))