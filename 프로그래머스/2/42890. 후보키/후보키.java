import java.util.*;

class Solution {
    public int solution(String[][] relation) {
        int answer = 0;
        Set<Integer> existingKey = new HashSet<>();
        
        int rowSize = relation.length;
        int colSize = relation[0].length;
        
        int totalCombianation = 1 << colSize;
        
        // mask가 5 -> 0101 -> 0, 2번째 칼럼 조합으로 검사하겠다.
        for (int mask = 1; mask < totalCombianation; mask++) {
            Set<String> keySet = new HashSet<>();
            
            // 튜플 순회
            for (int i = 0; i < rowSize; i++){
                
                String colString = "";
                
                for (int j = 0; j < colSize; j++){
                    // (1 << j) j번째만 1로 뜨게
                    if ((mask & (1 << j)) > 0){
                        colString = colString + relation[i][j] + ",";
                    }
                }
                keySet.add(colString);
                
            }
            if (keySet.size() == rowSize) {
                // 최소성 판단: 지금 추가하려는 것이 existingKey안에 있는 것을 부분집합으로 가지고 있는지 확인
                boolean flag = true;
                for (int e : existingKey) {
                    // e와 mask가 and 연산 한 것이 e 와 같으면 e가 mask의 부분집합이다.  
                    if ((e & mask) == e) {
                        flag = false;
                        break;
                    }
                }
                if (flag) existingKey.add(mask);
            }
        }
        answer = existingKey.size();
        return answer;
    }
}