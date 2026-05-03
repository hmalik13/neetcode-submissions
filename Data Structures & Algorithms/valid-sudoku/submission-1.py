class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # values in hashmaps are list of numbers in that
        # row, column, or square
        cols = defaultdict(set) # key: column index 
        rows = defaultdict(set) # key: row index
        squares = defaultdict(set)  # key: (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                   board[r][c] in cols[c] or 
                   board[r][c] in squares[(r // 3, c // 3)]):
                   return False
                # defaultdict allows us to add to the list 
                # in the hashmap even if its empty
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
