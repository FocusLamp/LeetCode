# Backtraking
# Time Complexity: O(n)

class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        count = Counter(nums)
        groups = [] # list of dictionaries
        visit = set()
        cache = {}

        def helper(number, group):
            if number not in group:
                return 1
            
            if number in cache:
                return cache[number]


            # two cases: Skip or Include it
            skip = helper(number + k, group)

            count = group[number] # All the possible groups
            include = (2 ** count - 1) * helper(number + 2 * k, group)
            
            # cache the result
            cache[number] = skip + include  

            return skip + include
        


        for number in count.keys():
            if number in visit:
                continue
            g = {}
            while number - k in count:
                number -= k
            
            while number in count:
                g[number] = count[number]
                visit.add(number)
                number += k
            
            groups.append(g)
        
        result = 1 # 1 is the nutural value so when it's muptiplied it won't stuck on zero

        for g in groups:
            number = min(g.keys())
            result = result * helper(number, g)
        
        return result - 1