class Solution(object):
    def minEatingSpeed(self, piles, h):
        #Binary Search bounds
        low = 1
        high = max(piles)

        #Helper: check if koko can finish at speed k
        def canfinish(k):
            hours = 0
            for p in piles:
                hours += (p+k-1)//k
                if hours > h:
                    return False
                return hours <= h
        while low<high:
            mid = (low+high)//2
            if canfinish(mid):
                high = mid #mid works, try smaller speed
            else:
                low = mid + 1 #mid too small, need faster speed
        return low
        

        
    
sol = Solution()
print(sol.minEatingSpeed(piles = [3, 6, 7, 11],h = 8))