import java.util.*;

class Solution {
    public int solution(int[][] info, int n, int m) {
        int answer = -1;
        // int[i][j] dp : i번째 물건까지 봤을 때, a의 흔적이 j개이고, B의 흔적의 최솟값
        
        int infoSize = info.length;
        int[][] dp = new int[infoSize+1][n];
        
        // 큰 값으로 초기화
        for ( int i = 0; i <= infoSize; i++) {
            Arrays.fill(dp[i], 999999);
        }
        
        // 시작점 정의
        dp[0][0] = 0;
        
        for (int i = 1; i <= infoSize; i++) {
            int aTrace = info[i-1][0];
            int bTrace = info[i-1][1];
            
            for(int j = 0; j < n; j++){
                
                // i 번째 물건을 A가 훔치는 경우
                int selectA = 999999;
                // 이전상태에서 j - aTrace 여야 지금 A의 흔적이 j가 됨
                if(j - aTrace >= 0) {
                    // 이전의 흔적값 그대로 가져옴. A가 훔치니까 B의 흔적값에 더할 필요 X
                    selectA = dp[i-1][j - aTrace];
                }
                
                // i번째 물건을 B가 훔치는 경우
                // 이전 흔적값에지금 흔적값 더해서 저장
                int selectB = dp[i-1][j] + bTrace;
                
                dp[i][j] = Math.min(selectA, selectB);
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (dp[infoSize][i] < m) {
                answer = i;
                break;
            }
        }
        
        return answer;
    }
}