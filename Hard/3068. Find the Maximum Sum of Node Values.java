// Greedy (Sorting Based Approch)
// Time complexity: O(n log n)
// Space complexity: O(n)

import java.util.Arrays;

class Solution {
    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        int N = nums.length;
        int[] net_change = new int[N];
        long node_sum = 0;

        for (int i = 0; i < N; i++) {
            net_change[i] = (nums[i] ^ k) - nums[i];
            node_sum += nums[i];
        }

        Arrays.sort(net_change);
        // Reverse the sorted array
        for (int i = 0; i < N / 2; i++) {
            int temp = net_change[i];
            net_change[i] = net_change[N - 1 - i];
            net_change[N - 1 - i] = temp;
        }

        for (int i = 0; i < N; i += 2) {
            // if net_change contains odd number of elements we break the loop
            if (i + 1 == N) {
                break;
            }

            long pair_sum = net_change[i] + net_change[i + 1];
            // include in node_sum if pair_sum is positive (more than 0)
            if (pair_sum > 0) {
                node_sum += pair_sum;
            }
        }

        return node_sum;

    }
}
