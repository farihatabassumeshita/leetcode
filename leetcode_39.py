class Solution(object):
    def combinayion(self, candidates, target):
        res = []
        def backtrack(i, current_sum, total):
            #base case 1: if total == target
            if total == target:
                res.append(list(current_sum))
                return
            #base case 2: if total >= target or ran out of index nums
            if total >= target or i >= len(candidates):
                return
            
            #choice 1: include canditates[i]
            current_sum.append(candidates[i])
            backtrack(i, current_sum, candidates[i] + total)
            current_sum.pop()

            #choice 2: exclude canditates[i]
            backtrack(i+1, current_sum, total)
        backtrack(0,[],0)
        return res