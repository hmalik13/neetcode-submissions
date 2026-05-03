class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = collections.deque()
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        length = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                directions = [[0,1], [0,-1], [1,0], [-1, 0]]
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c

                    if (min(row, col) < 0 or 
                        row == ROWS or col == COLS or
                        grid[row][col] == 1 or
                        (row, col) in visited):
                        continue
                    q.append((row, col))
                    visited.add((row, col))
            length += 1
        return -1