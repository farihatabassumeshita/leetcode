class Solution(object):
    
    def sudokusolver(self, board):
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        empty = []
        b = (r//3)*3 + (c//3)

        #initialize sets for given numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r,c))
                num = board[r][c]
                row[r].add(num)
                col[c].add(num)
                box[b].add(num)

        def backtrack(i=0):
            if i == len(empty):
                return True
            r,c = empty[i]
            for num in map(str, range(1,10)):
                if num not in row[r] and num not in col[c] and num not in box[b]:
                    board[r][c] = num
                    row[r].add(num)
                    col[c].add(num)
                    box[b].add(num)
                    if backtrack(i+1):
                        return True
                    board[r][c] = "."
                    row[r].remove(num)
                    col[c].remove(num)
                    box[b].remove(num)
                return False
        backtrack()
        return board


    # Time exceed
    # def solveSuoku(self, board):
    #     def is_valid(r, c, num):
    #         #check row
    #         for i in range(9):
    #             if board[r][i] == num:
    #                 return False
    #         #check col
    #         for i in range(9):
    #             if board[i][c] == num:
    #                 return False
    #         # check 3*3
    #         box_r, box_c = (r//3)*3, (c//3)*3
    #         for i in range(3):
    #             for j in range(3):
    #                 if board[box_r+i][box_c+j] == num:
    #                     return False
    #         return True

    #     def backtrack():
    #         for r in range(9):
    #             for c in range(9):
    #                 if board[r][c] == ".":
    #                     for num in map(str, range(1,10)):
    #                         if is_valid(r, c, num):
    #                             board[r][c] = num
    #                             if backtrack():
    #                                 return True
    #                             board[r][c] = "."
    #                     return False
    #         return True
    #     backtrack()