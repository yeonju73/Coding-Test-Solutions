class Solution {
    public long solution(int n) {
        if (n==1) return 1;
        
        int[] dp = new int[n];
        
        // dp[n] = n에 도달하는 경우의 수
        
        dp[0] = 1; // 1칸
        dp[1] = 2; // (1칸, 1칸) or (2칸)
        
        for (int i = 2; i < n; i++) {
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567;
        }
        
        return dp[n-1];
    }
}