import java.util.ArrayList;

class Solution {
    public void reverseString(char[] s) {
        ArrayList<Character> stack = new ArrayList<>();
        for (int i = s.length - 1; i >= 0; i--) {
            stack.add(s[i]);
        }

        for (int i = 0; i < s.length; i++) {
            s[i] = stack.remove(0);
        }

    }   
}