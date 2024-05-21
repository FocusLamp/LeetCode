// Bit Manipulation
// Time compelxity: O(n)
// Space compelxity: O(1)
class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int result = 0;

        // Capture each bit that is set in any of the elements
        for (int num : nums) {
            result = result | num;
        }

        // Multiply by the number of subsets XOR totals that will have each bit set
        return result << ((nums.size() - 1));
    }
};