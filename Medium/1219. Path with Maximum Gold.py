"""
THERE'S AN ERROR BY ONE IN THIS EXAMPLE
[[0,6,0],[5,8,7],[0,9,0]]
Output
23
Expected
24
"""

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [0, 1, 0, -1, 0]
        rows = len(grid)
        cols = len(grid[0])
        max_gold = 0

        def dfs(grid, rows, cols, row, col):
            # Base case: the cell is out of bounds or has 0 gold
            if row < 0 or col < 0 \
            or row == rows or col == cols or grid[row][col] == 0:
                return 0
            
            max_gold = 0
            

            # Mark the cell as visited and save the value
            original_val = grid[row][col]
            grid[row][col] = 0


            # Backtracking in each of the four directions
            for direction in range(4):
                max_gold = max(
                    max_gold,
                    dfs(grid, rows, cols,
                        DIRECTIONS[direction] + row,
                        DIRECTIONS[direction + 1] + col
                    )
                )

            # Search for the path with the maximum gold starting from each cell
            for row in range(rows):
                for col in range(cols):
                    max_gold = max(
                        max_gold,
                        dfs(grid, rows, cols, row, col)
                    )
            
            return max_gold
