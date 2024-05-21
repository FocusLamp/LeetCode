// Optimized Backtraking
// Time Complexity: O(2^n)
// Space Complexity: O(n)
class Solution {
    public int subsetXORSum(int[] nums) {
        return XORSum(nums, 0, 0);
    }

    private int XORSum(int[] nums, int index, int currentXOR) {
        // Return currentXOR when all the elements are traversed
        if (index == nums.length)
            return currentXOR;

        // Calculate sum of subset XOR with current element
        int with_element = XORSum(nums, index + 1, currentXOR ^ nums[index]);

        // Calculate sum of subset XOR without current element
        int without_element = XORSum(nums, index + 1, currentXOR);

        // return sum of XOR totals
        return with_element + without_element;

    }
}
