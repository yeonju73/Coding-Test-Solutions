import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        char[] word = s.toCharArray();
        char[] skipArray = skip.toCharArray();
        Set<Character> my_set = new HashSet<>();
        
        for (char c : skipArray) {
            my_set.add(c);
            // System.out.print(c);
        }
        System.out.println();
        for (int j = 0; j < word.length; j++) {
            char c = word[j];
            for (int i = 1; i <= index; i++) {
                c += 1;
                if (c > 'z') {
                    c = 'a';
                }
                // System.out.println(i + " : " + c);
                
                // skip 문자 중에 하나라면
                while (my_set.contains(c)) {
                    // System.out.println(c + " contains myset");
                    c += 1;
                    if (c > 'z') {
                        c = 'a';
                    }
                }
            }
            word[j] = c;
            // System.out.println("word " + j + ": " + c);
        }
        
        answer = String.valueOf(word);
        return answer;
    }
}