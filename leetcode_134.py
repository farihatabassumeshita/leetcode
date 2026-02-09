class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        curTank = totalTank = start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            curTank += diff
            totalTank += diff
            if curTank < 0:
                start = i+1
                curTank = 0
        return start if totalTank >= 0 else -1