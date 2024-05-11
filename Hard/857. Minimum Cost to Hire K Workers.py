from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        N = len(quality)
        total_cost = float("inf")
        current_total_quality = 0

        wage_to_quality_ratio = []

        # Wage-to-quality ratio for every worker

        for i in range(N):
            wage_to_quality_ratio.append((wage[i] / quality[i], quality[i]))

        
        # Sort workers based on thier ratio-to-quality ratio
        wage_to_quality_ratio.sort(key=lambda x: x[0])

        # Using heaps to keep track of the highest quality workers
        highest_quality_workers = []

        # Iterate through all workers
        for i in range(N):
            heapq.heappush(highest_quality_workers, -wage_to_quality_ratio[i][1])
            current_total_quality += wage_to_quality_ratio[i][1]

            # If there is more than k workers
            # Remove the one with highest quality
            if len(highest_quality_workers) > k:
                current_total_quality += heapq.heappop(highest_quality_workers)
            
            
            
            # If there is exactly k workers
            # calculate the total cost and update it if it's minimum
            if len(highest_quality_workers) == k:
                total_cost = min(
                    total_cost, current_total_quality * wage_to_quality_ratio[i][0]
                )
        
        return total_cost
