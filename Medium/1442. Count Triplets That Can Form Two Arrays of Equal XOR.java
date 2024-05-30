class Solution {
    public int countTriplets(int[] arr) {
        
        int[] prefixXOR = new int[arr.length + 1];
        prefixXOR[0] = 0;
        System.arraycopy(arr, 0, prefixXOR, 1, arr.length);
        
        int size = prefixXOR.length;

        // perform XOR on consecutive elements in the modified array
        for (int i = 1; i < size; i++) {
            prefixXOR[i] ^= prefixXOR[i - 1];
        }

        int count = 0;

        // iterate througth the modified array to count triplets
        for (int start = 0; start < size; start++) {
            for (int end = start + 1; end < size; end ++) {
                if (prefixXOR[start] == prefixXOR[end]) {
                    count += end - start - 1;
                }
            }
        }

        return count;
    }
}