class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        size = len(arr) 
        count = 0
        prefix = 0
        
        # count the number of triplets
        count_map = defaultdict(int)
        count_map[0] = 1
        total_map = defaultdict(int)

        # Iterate through the array
        for i in range(size):
            # Calculating XOR prefix
            prefix ^= arr[i]


            # calculating contribution of current element to hte result
            count += count_map[prefix] * i - total_map[prefix]

            # Updating total count of current XOR value
            total_map[prefix] += i + 1
            count_map[prefix] += 1
        
        return count
