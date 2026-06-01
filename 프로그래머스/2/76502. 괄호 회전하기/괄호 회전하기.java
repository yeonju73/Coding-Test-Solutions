import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        Stack<Character> stack;
        Map<Character, Character> map = new HashMap<>();
        
        map.put(']', '[');
        map.put(')', '(');
        map.put('}', '{');
        
        String double_string = s + s;
        
        for (int i = 0; i < s.length(); i++) {
            
            stack = new Stack<>();
            
            for (int j = i; j < i+s.length(); j++) {
                char value = map.getOrDefault(double_string.charAt(j), 'N');
                
                if (!stack.isEmpty() && (stack.peek() == value)) {
                    stack.pop();
                } else {
                    stack.push(double_string.charAt(j));
                }
            }
            if (stack.isEmpty()) answer++;
        }        
        return answer;
    }
}