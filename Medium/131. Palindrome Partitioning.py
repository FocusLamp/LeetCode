class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        lenS = len(s)

        def search_for_palindrome(index, curr):
            if index >= lenS:
                result.append(curr.copy())

            for i in range(index, lenS):
                subStr = s[index:i + 1]
                if subStr == subStr[::-1]:
                    curr.append(subStr)
                    search_for_palindrome(i + 1, curr)
                    curr.pop()

        search_for_palindrome(0, [])
        return result