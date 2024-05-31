class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int x = 0;
        for (int num : nums) {
            x ^= num;
        }
        int rightmost_set_bit = x & ~(x - 1);
        int a = 0, b = 0;
        for (int num : nums) {
            if (num & rightmost_set_bit) {
                a ^= num;
            } else {
                b ^= num;
            }
        }
        return {a, b};
    }
};