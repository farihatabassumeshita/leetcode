from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        #step 1: Count fresh and collect all rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0)) #row, col, min
                elif grid[r][c] == 1:
                    fresh += 1
        #edge case: no fresh oranges
        if fresh == 0:
            return 0

        #step 2: BFS
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        time = 0
        while q:
            r, c, t = q.popleft()
            time = max(time,t) #track max mins
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<= nr < rows and 0<= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2 #make it rotten
                    fresh -= 1
                    q.append((nr,nc, t+1))

        #step 3: check if all fresh oranges rotted
        return time if fresh == 0 else -1
