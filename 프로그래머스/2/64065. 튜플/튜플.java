import java.util.*;

class Solution {
    public List<Integer> solution(String s) {
        StringTokenizer st;
        
        st = new StringTokenizer(s.substring(2, s.length()-2), "}");
        int size = st.countTokens();
        
        Map<Integer, Integer> map = new HashMap<>();
        
        st = new StringTokenizer(s.substring(2, s.length()-2), "{},");
        
        int n = st.countTokens();
        
        for(int i = 0; i < n; i++) {
            int next = Integer.parseInt(st.nextToken());
            map.put(next, map.getOrDefault(next, 0)+1);
        }
        
        List<Integer> keyList = new ArrayList<>(map.keySet());
        Collections.sort(keyList, (k1, k2) -> map.get(k2).compareTo(map.get(k1)));
                
        return keyList;
    }
}