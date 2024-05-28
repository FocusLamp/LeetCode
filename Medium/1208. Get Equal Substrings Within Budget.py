class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        currentCost = 0
        left = 0
        result = 0


        for right in range(len(s)):
            currentCost = currentCost + abs(ord(s[right]) - ord(t[right]))
            

            while currentCost > maxCost:
                currentCost = currentCost - abs(ord(s[left]) - ord(t[left]))
                left = left + 1

            result = max(result, right - left + 1)


        return result
