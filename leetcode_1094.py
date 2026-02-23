class Solution(object):
    def carPooling(self, trips, capacity):
        event = []
        for p, start, end in trips:
            event.append((start,p)) #pick up
            event.append((end,-p)) #drop off
        event.sort()
        curr = 0
        for _, passenger in event:
            curr += passenger
            if curr > capacity:
                return False
        return True    
    
sol = Solution()
print(sol.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4))
            
                