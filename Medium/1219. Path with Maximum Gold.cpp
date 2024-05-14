
class Solution
{
public:
    int getMaximumGold(vector<vector<int>> &grid)
    {
        int rows = grid.size();
        int cols = grid[0].size();
        int maxGold = 0;

        // Search for the path with the maximum gold starting from each cell
        for (int row = 0; row < rows; row++)
        {
            for (int col = 0; col < cols; col++)
            {
                maxGold = max(
                    maxGold,
                    dfsBacktrack(grid, rows, cols, row, col)
                    );
            }
        }
        return maxGold;
    }

private:
    const vector<int> DIRECTIONS = {0, 1, 0, -1, 0};

    int dfsBacktrack(vector<vector<int>> &grid, int rows, int cols, int row, int col)
    {
        // Base case: this cell is out of bounds or has 0 gold
        if (row < 0 || col < 0 || row == rows || col == cols || grid[row][col] == 0)
        {
            return 0;
        }
        int maxGold = 0;

        // Mark this cell as visited and search the value
        int originalVal = grid[row][col];
        grid[row][col] = 0;

        // Backtrack in all possible directions to find the maximum gold
        for (int direction = 0; direction < 4; direction++)
        {
            maxGold =
                max(maxGold,
                    dfsBacktrack(grid, rows, cols, DIRECTIONS[direction] + row, DIRECTIONS[direction + 1] + col));
        }

        // Set the cell back to its original value
        grid[row][col] = originalVal;

        return maxGold + originalVal;
    }
};