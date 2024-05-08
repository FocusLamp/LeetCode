class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        my_sorted_score = sorted(score, reverse=True)
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = []
        
        for i in range(3, len(score)):
            ranks.append(str(i + 1))
        
        for s in score:
            index = my_sorted_score.index(s)
            result.append(ranks[index])
        
        return result