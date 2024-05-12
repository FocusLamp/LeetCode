class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        result = [[0] * (N - 2) for _ in range(N - 2)]

        for i in range(N - 2):
            for j in range(N - 2):
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        result[i][j] = max(
                            result[i][j],
                            grid[row][col]
                        )
        
        return result