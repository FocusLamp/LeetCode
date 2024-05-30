class Solution {
public:
    int countTriplets(vector<int>& arr) {
        int count = 0;
        // iterating thorough the possible starting index i
        for (int start = 0; start < arr.size(); ++start) {
            // xorA from the start of the array to the mid - 1
            int xorA = 0;

            // iterate thorough each possible index j
            for (int mid = start + 1; mid < arr.size(); ++mid) {
                // update xorA to include arr[mid - 1]
                xorA ^= arr[mid - 1];

                // create xorB for the subarray from mid to the end ot the array
                int xorB = 0;

                for (int end = mid; end < arr.size(); ++end) {
                    xorB ^= arr[end];

                    // found triplet (start, mid, end)
                    if (xorA == xorB) {
                        ++count;
                    }
                }
            }
        }

        // return number of triplets
        return count;
    }
};