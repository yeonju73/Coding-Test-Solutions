import java.util.*;
class Solution {
    public int solution(int[][] info, int n, int m) {
        final int INF = 100000;
        
        int[] dp = new int[m]; // dp[j]: B의 흔적이 j개일때 A흔적의 최솟값
        Arrays.fill(dp, INF);
        dp[0] = 0; // 흔적이 0개일 때 A흔적의 최솟값은 0
        
        for(int[] item : info) {
            int a = item[0];
            int b = item[1];
            
            int[] nextDp = new int[m];
            Arrays.fill(nextDp, INF);
            
            for(int j=0; j<m; j++) {
                if(dp[j] == INF) continue;
                
                nextDp[j] = Math.min(nextDp[j], dp[j]+a); // A가 훔칠경우 (B흔적 j는 유지, A흔적 a를 추가)
                
                if(j+b<m) {
                    nextDp[j+b] = Math.min(nextDp[j+b], dp[j]);
                }
            }
            dp = nextDp;
        }
        
        // B의 흔적이 m 미만인 경우 중, A의 흔적이 n 미만인 최솟값 탐색
        int answer = INF;
        for (int j = 0; j < m; j++) {
            if (dp[j] < n) {
                answer = Math.min(answer, dp[j]);
            }
        }

        return answer == INF ? -1 : answer;
    }
}