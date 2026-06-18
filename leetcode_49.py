from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        hash_map = defaultdict(list)
        for s in strs:
            sort_s = ''.join(sorted(s))
            hash_map[sort_s].append(s)
        return list(hash_map.values())
    
    def groupAnagramsHash(self, strs):
        hash_map = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hash_map[tuple(count)].append(s)
        return list(hash_map.values())

sol = Solution()
print(sol.groupAnagramsHash(strs = ["eat","tea","tan","ate","nat","bat"]))