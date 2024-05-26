class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = {}


        def backTrack(i):
            if i == len(s):
                return [""]
            
            result = []

            for j in range(len(s)):
                word = s[i: j + 1]
                if word not in wordDict:
                    continue

                strings = backTrack(j + 1)

                if not strings:
                    continue

                for sub_string in strings:
                    sentence = word 
                    if sub_string:
                        sentence += " " + sub_string
                    result.append(sentence)
                
            cache[i] = result
            return result
        
        return backTrack(0)