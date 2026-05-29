import java.util.*;

class Solution {
    public int solution(String s) {
        StringBuilder sb = new StringBuilder();
        List<String> words = new ArrayList<>(List.of(
            "zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine"
        ));
        
        char[] word_list = s.toCharArray();
        
        int i = 0;
        while (i < word_list.length) {
            // 숫자일때
            if (word_list[i] >= '0' && word_list[i] <= '9'){
                sb.append(word_list[i]);
            } 
            else {
                StringBuilder stringBuilder = new StringBuilder();
                while(true) {
                    stringBuilder.append(word_list[i]);
                    String check = stringBuilder.toString();
                    
                    if (words.contains(check)) {
                        sb.append(words.indexOf(check));
                        break;
                    }
                    i++;
                }
            }
            i++;
        }
        
        return Integer.parseInt(sb.toString());
    }
}