// 장르: 플레이 수
import java.util.*;

class Solution {
    public ArrayList<Integer> solution(String[] genres, int[] plays) {
        int n = genres.length;
        
        Map<String, Integer> myMap = new HashMap<>();
        Map<String, ArrayList<Integer>> indexMap = new HashMap<>();        
        
        for(int i = 0; i < n; i++) {
            myMap.put(genres[i], myMap.getOrDefault(genres[i], 0) + plays[i]);
            indexMap.computeIfAbsent(genres[i], k -> new ArrayList<>());
            indexMap.get(genres[i]).add(i);
        }

        List<String> keyList = new ArrayList<>(myMap.keySet());
        Collections.sort(keyList, (k1, k2) -> myMap.get(k2).compareTo(myMap.get(k1)));
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (String k : keyList){
            
            int max = -1;
            int second = -1;
            
            for (int i : indexMap.get(k)) {
                if (max == -1 || plays[i] > plays[max]) {
                    second = max;
                    max = i;
                }
                else if (second == -1 || plays[i] > plays[second]) {
                    second = i;
                }
            }
            answer.add(max);
            if (second != -1) answer.add(second);
        }
        return answer;
    }
}