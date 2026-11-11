// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int N) {
        int longestGap = 0;
        int currentGap = 0;

        while (N > 0 && N % 2 == 0) {
            N = N / 2;
        }

        // Count zeros between ones
        while (N > 0) {
            if (N % 2 == 0) {
                currentGap++;
            } else {
                longestGap = Math.max(longestGap, currentGap);
                currentGap = 0;
            }

            N = N / 2;
        }

        return longestGap;
    }
}
    

