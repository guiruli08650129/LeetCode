class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def find(grid, i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 0:
                grid[i][j] = 0
                return find(grid, i, j+1)+find(grid, i, j-1)+find(grid, i+1, j)+find(grid, i-1, j)+1
            return 0
        maxland = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxland = max(maxland, find(grid, i, j))
        return maxland