// Sliding window
// Time Complexity = O(n)
// Space Complexity = O(1)

class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        
        int N = s.length();
        
        // the length of the window
        int maxLen = 0;
        
        // the index which the window start at
        int start = 0;
        
        // the total cost of the window
        int currentCost = 0;

        for (int i = 0; i < N; i++) {
            // Add the current index to the sub-string
            currentCost = currentCost + Math.abs(s.charAt(i) - t.charAt(i));

            // Remove the indices from the left of the window until the currentCost becomes less than or equal to the maxCost
            while (currentCost > maxCost) {
                currentCost = currentCost - Math.abs(s.charAt(start) - t.charAt(start));
                start++;
            }

            // Update the maxLen
            maxLen = Math.max(maxLen, i - start + 1);
        }

        // Return the length of the window
        return maxLen;
    }
}
