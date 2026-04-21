class Solution(object):
    def findContentChildren(self, g, s):
        i, j, count= 0, 0, 0
        while i<len(g) and j<len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                i += 1
                j += 1
        return count
sol = Solution()
print(sol.findContentChildren(g = [1,2], s = [1,2,3]))