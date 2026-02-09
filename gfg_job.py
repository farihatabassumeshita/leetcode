class Solution(object):
    def jobsequencing(self, deadline, profit):
        # create #(deadline, profit, index)
        job = [(deadline[i], profit[i], i+1) for i in range(len(deadline))]
        # sort jobs in decending order
        job.sort(key=lambda x:x[1], reverse=True)
        # slot array (1-based indexing) 
        slot = [False] * (max(deadline)+1)
        count, total_profit = 0, 0
        # assign jobs
        for d,p,idx in job:
            # try to place job in latest available slot <= deadline
            for t in range(d, 0, -1):
                if not slot[t]:
                    slot[t] = True
                    count += 1
                    total_profit += p
                    break
        return [count,total_profit]


sol = Solution()
print(sol.jobsequencing(deadline= [4, 1, 1, 1], profit= [20, 10, 40, 30]))