// Greedy (Finding local maxima and minima)
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution {
public:
   long long maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {

    long long sum = 0;
    int count = 0;
    int positive_minimum = (1 << 30);
    int negative_maximum = -1 * (1 << 30);

    
    for (int node_value : nums) {
        int operated_node_value = node_value ^ k;
        sum += node_value;
        int net_change = operated_node_value - node_value;

        if (net_change > 0) {
            positive_minimum = min(positive_minimum, net_change);
            sum += net_change;
            count++;
        } else {
            negative_maximum = max(negative_maximum, net_change);
        }
    }


    // if the number of positive net_change values is even return the sum
    if (count % 2 == 0) {
        return sum;
    }

    // otherwise return the maximum of both negative_maximum and positive_minimum
    return max(sum - positive_minimum, sum + negative_maximum);

    }
};
