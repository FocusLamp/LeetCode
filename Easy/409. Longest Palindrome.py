class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        result = 0

        for char in s:
            if char in seen:
                seen.remove(char)
            else:
                seen.add(char)
        

        for count in count.values():
            if count % 2:
                result += 1
                break

        return result