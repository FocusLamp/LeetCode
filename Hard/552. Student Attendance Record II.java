class Solution {
    public int checkRecord(int n) {
        int MOD = 1000000007;
        // cache for the current sub-problem
        int[][] dpCurrentState = new int[2][3];
        //cache for the next sub-problem
        int[][] dpNextState = new int[2][3];

        // Base case, one string of length 0 with zero "A" and zero "L"
        dpCurrentState[0][0] = 1;

        // Iterate on smaller sub-problems and use the current smaller sub-problem to generate results for the next sub-problem.
        for (int len = 0; len < n; ++len) {
            for (int totalAbsences = 0; totalAbsences <= 1; ++totalAbsences) {
                for (int consecutiveLates = 0; consecutiveLates <= 2; ++consecutiveLates) {
                    
                    // Store the count when "P" is chosen
                    dpNextState[totalAbsences][0] = (dpNextState[totalAbsences][0] + dpCurrentState[totalAbsences][consecutiveLates]) % MOD;


                    // Store the count when "L" is chosen
                    if (consecutiveLates < 2) {
                        dpNextState[totalAbsences][consecutiveLates + 1] = (dpNextState[totalAbsences][consecutiveLates + 1] + dpCurrentState[totalAbsences][consecutiveLates]) % MOD;
                    }

                    if (totalAbsences < 1) {
                        // Store the count when "A" is chosen
                        dpNextState[totalAbsences + 1][0] = (dpNextState[totalAbsences + 1][0] + dpCurrentState[totalAbsences][consecutiveLates]) % MOD;
                    }
                }
            }

            // Next sub-problem will becomes the current sub-problem on the next iteration
            System.arraycopy(dpNextState, 0, dpCurrentState, 0, dpCurrentState.length);
            // dp next state sub-problem sub-problem result will reset to ZERO
            dpNextState = new int[2][3];
        }


        // Sum up all the counts for all combinations of length "n" with different number of "A" and "L"
        int count = 0;
        for (int totalAbsences = 0; totalAbsences <= 1; ++totalAbsences) {
            for (int consecutiveLates = 0; consecutiveLates <= 2; ++consecutiveLates) {
                
                count = (count + dpCurrentState[totalAbsences][consecutiveLates]) % MOD;

            }
        }

        return count;

    }
}