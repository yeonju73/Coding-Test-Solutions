import java.util.*;

class Solution {
    public Integer[] solution(int N, int[] stages) {
        double[] answer = new double[N];
        Map<Integer, Integer> userStageMap = new HashMap<>();
        
        for (int i = 1; i <= N+1; i++) {
            userStageMap.put(i, 0);
        }
        
        for (int f : stages) {
            userStageMap.put(f, userStageMap.get(f) + 1);
        }
                
        // 시도한 사람 수
        int temp = userStageMap.get(N+1);
        
        for (int i = N; i >= 1; i--) {
            temp += userStageMap.get(i);
            if (userStageMap.get(i) == 0) 
                answer[i-1] = 0;
            else
                answer[i-1] = ((double)userStageMap.get(i) / temp);
        }
                
        Integer[] stageIds = new Integer[N];
        
        for (int i = 0; i < N; i++) {
            stageIds[i] = i + 1;
        }
        
        Arrays.sort(stageIds, (k1, k2) -> {
            if (answer[k2 - 1] == answer[k1 - 1])
                return k1 - k2;
            return Double.compare(answer[k2 - 1], answer[k1 - 1]);
        });
        
        return stageIds;
    }
}