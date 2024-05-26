class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        // Convert wordDict to a set for O(1) lookup
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<string> results;
        string currentSentence;
        // Start the backtracking
        backtrack(s, wordSet, currentSentence, results, 0);
        return results;
    }



private:
    void backtrack(const string& s, const unordered_set<string>&wordSet, string& currentSentence, vector<string>& results, int startIndex) {
        // Base case: we have reached the end of the string
        // Add the current string to the result
        if (startIndex == s.length()) {
            results.push_back(currentSentence);
            return;
        }

        // Iterate over possible end indices
        for (int endIndex = startIndex + 1; endIndex <= s.length(); ++endIndex) {
            string word = s.substr(startIndex, endIndex - startIndex);
            // If the word is in the substring, continue with the backtrack
            if (wordSet.find(word) != wordSet.end()) {
                string originalSentence = currentSentence;
                if (!currentSentence.empty()) currentSentence += " ";
                currentSentence += word;
                // Recursively call backtrack with the new end index
                backtrack(s, wordSet, currentSentence, results, endIndex);
                
                // Reset currentSentence to it's original state (value)
                currentSentence = originalSentence;
            }
        }
    };
};