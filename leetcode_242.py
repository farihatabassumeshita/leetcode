import heapq
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        count_s = Counter(s) #(word, freq)
        count_t = Counter(t) #(word, freq)
        return count_s == count_t
    
sol = Solution()
print(sol.isAnagram(s = "rat", t = "car"))
            
            
    