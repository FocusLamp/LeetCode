class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        dp = [0] * len(ring)
        
        for k in reversed(range(len(key))):
            
            current_dp = [float("inf")] * len(ring)
            
            for r in range(len(ring)):
                for i, char in enumerate(ring):
                    if char == key[k]:
                        min_dist = min(
                            abs(r - i),
                            len(ring) - abs(r - i)
                        )
                        current_dp[r] = min(
                            current_dp[r],
                            min_dist + 1 + dp[i]
                        )
            dp = current_dp
        return dp[0]
        
        
        
            
        # cache = {}

        # def helper(r, k):                   # RECURSIVE
        #     if k == len(key):
        #         return 0
        #     if (r, k) in cache:
        #         return cache[(r, k)]

        #     res = float("inf")
        #     for i, char in enumerate(ring):
        #         if char == key[k]:
        #             min_dist = min(
        #                 abs(r - i),             # Between
        #                 len(ring) - abs(r - i)  # Around
        #             )
        #             res = min(
        #                 res,
        #                 min_dist + 1 + helper(i, k + 1)
        #             )
        #     cache[(r, k)] = res

        #     return res
        # return helper(0, 0)
