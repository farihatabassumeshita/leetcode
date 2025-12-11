import heapq
from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        min_heap = []
        result = []
        count = Counter(s) #(letter, feq)
        for letter, freq in count.items():
            heapq.heappush(min_heap, (-freq, letter))
        while min_heap:
            freq, letter = heapq.heappop(min_heap)
            result.append(letter * -freq)
        return ''.join(result)

    
sol = Solution()
print(sol.frequencySort(s = "tree"))