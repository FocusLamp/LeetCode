class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        # First pass: XOR all numbers to get xor of the two unique numbers
        for n in nums:
            xor ^= n

        # Find the rightmost set bit in xor (diff_bit)
        diff_bit = 1
        while not (xor & diff_bit):
            diff_bit <<= 1

        a = 0
        b = 0

        # Second pass: Divide numbers into two groups based on diff_bit and XOR each group
        for n in nums:
            if n & diff_bit:  # Check if the bit at diff_bit position is set
                a ^= n
            else:
                b ^= n

        return [a, b]
