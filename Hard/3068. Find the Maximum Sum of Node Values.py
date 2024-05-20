# Bottom-up Dynamic Programming (Tabulation) 

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        N = len(nums)
        dp = [[0] * N for i in range(N + 1)]
        dp[N][1] = 0
        dp[N][0] = -float("inf")
        
        for index in range(N - 1, -1, -1):
            for is_even in range(2):
                # Case 1: We perform an operation on this element
                perform_operation = dp[index + 1][is_even ^ 1] + (nums[index] ^ k)
                
                # Case 2: We don't perform operation on this element
                dont_perform_operation = dp[index + 1][is_even] + nums[index]
                
                
                dp[index][is_even] = max(perform_operation, dont_perform_operation)
        
        return dp[0][1]
