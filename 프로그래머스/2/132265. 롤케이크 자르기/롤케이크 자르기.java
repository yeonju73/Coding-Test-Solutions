import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        
        Set<Integer> set = new HashSet<>();
        Map<Integer, Integer> map = new HashMap<>();
        
        // map 초기화, 토핑 종류랑 개수
        for (int i = 0; i < topping.length; i++) {
            map.put(topping[i], map.getOrDefault(topping[i], 0) + 1);
        }
        
        // 형이 모든 조각을 가지고 있다고 생각
        for (int i = topping.length - 1; i >= 0; i--) {
            set.add(topping[i]);
            
            // 가진 수가 0개가 되면 map 에서 remove
            if (map.get(topping[i]) == 1) {
                map.remove(topping[i]);
            } else {
                map.put(topping[i], map.get(topping[i])-1);
            }
                
            if (set.size() == map.size()) {
                answer++;
            }
        }
        
        return answer;
    }
}