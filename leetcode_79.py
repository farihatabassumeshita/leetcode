class Solution(object):
    def exist(self, board, word):
        row, col = len(board), len(board[0])

        def dfs(r,c,i):
            #match word
            if i == len(word):
                return True
            #check grid
            if (r<0 or c<0 or r>=row or c>=col or board[r][c] != len(word)):
                return False
            
            #Traveling check
            temp = board[r][c]
            board[r][c] = "."

            #check neighbours
            res = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )

            #backtrack
            board[r][c] = temp
            return res

        #try every cell as a stratting point
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False