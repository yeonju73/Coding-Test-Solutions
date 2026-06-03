import java.util.*;

class Solution {
    int solution(int[][] land) {
        int answer = 0;
        // dp[n][m] = n번째 줄에서 m을 밟았을 때 가질 수 있는 최대값
        int n = land.length;
        int m = land[0].length;
        
        int[][] dp = new int[n][m];
        int max = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i > 0){
                    for(int k = 0; k < m; k++) {
                        // 같은 열을 연속해서 밟을 수 없음
                        if (k != j)
                            max = Math.max(dp[i-1][k], max);
                    }
                }
                
                dp[i][j] = max + land[i][j];
                max = 0;
            }
            
        }
        for(int k = 0; k < m; k++) {
            max = Math.max(dp[n-1][k], max);
        }
        return max;
    }
}