import java.util.*;

class Solution {
    public int solution(int[] elements) {
        
        int[] circle_elements = new int[elements.length * 2];
        System.arraycopy(elements, 0, circle_elements, 0, elements.length);
        System.arraycopy(elements, 0, circle_elements, elements.length, elements.length);

        Set<Integer> answer = new HashSet<>();
        
        // dp[i]는 길이 len인 수열의 i부터 i+len까지 더한 값
        // dp[i] = dp[i] + circle_elements[i + len]
        int[] dp = new int[elements.length];
        
        // len 0 일때는 길이 1인 수열 -> for 문 돌면서 점차 길이가 긴 수열의 합
        for (int len = 0; len < elements.length; len++) {
            for (int i = 0; i < elements.length; i++) {
                dp[i] += circle_elements[i + len];
                answer.add(dp[i]);
            }
        }
        
        return answer.size();
    }
}