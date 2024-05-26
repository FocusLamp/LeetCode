import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {

        // map the results of the subproblems
        Map<Integer, List<String>> dp = new HashMap<>();
        
        // iterate from the end of the current string "s" to the beginning
        for (int startIndex = s.length(); startIndex >= 0; startIndex--) {
            // Create a list to store the valid sentences starting from "startIndex"
            List<String> validSentences = new ArrayList();

            for (int endIndex = startIndex; endIndex < s.length(); endIndex++) {
                String currentWord = s.substring(startIndex, endIndex + 1);

                // check if the current substring is a valid word in the dictionary
                if (isWordInDict(currentWord, wordDict)) {
                    // if it's the last word add it as a "valid sentence"
                    if (endIndex == s.length() - 1) {
                        validSentences.add(currentWord);
                    } else {
                        // if it's not the last word, add it to the list of valid sentences
                        List<String> sentencesFromNextIndex = dp.get(endIndex + 1);
                            for (String sentence : sentencesFromNextIndex) {
                                validSentences.add(currentWord + " " + sentence);
                        }
                    }
                }
            }
            // Store the valid sentences in dp
            dp.put(startIndex, validSentences);
        }
        // Return the sentences formed from the entire string
        return dp.getOrDefault(0, new ArrayList<>());
    }

    // Helper function to check if a the word is in the dictionary
    private boolean isWordInDict(String word, List<String> wordDict) {
        return wordDict.contains(word);
    }
}
