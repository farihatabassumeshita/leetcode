from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        q = deque()

        #Step 1: Push all 0 in queue, mark 1s as infinity
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = float('inf')

        #Step 2: BFS Expansion
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r,c = q.popleft()
            for dr, dc in direction:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if mat[nr][nc] > mat[r][c] + 1:
                        mat[nr][nc] = mat[r][c] + 1
                        q.append((nr,nc))        
        return mat
    
sol = Solution()
print(sol.updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]]))