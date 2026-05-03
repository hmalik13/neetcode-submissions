class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.dfs(grid, 0, 0, set())

    def dfs(self, grid, r, c, visit):
        rows = len(grid)
        cols = len(grid[0])

        # check for invalid path
        if r == rows or c == cols or (r, c) in visit or min(r, c) < 0 or grid[r][c] == 1:
            return 0
            
        # check for valid path
        if r == rows - 1 and c == cols - 1:
            return 1
            
        # add visited cell to hash set
        visit.add((r, c))

        # try moving in each direction
        count = 0
        count += self.dfs(grid, r+1, c, visit)
        count += self.dfs(grid, r-1, c, visit)
        count += self.dfs(grid, r, c+1, visit)
        count += self.dfs(grid, r, c-1, visit)

        # backtrack
        visit.remove((r, c))
        return count

            

