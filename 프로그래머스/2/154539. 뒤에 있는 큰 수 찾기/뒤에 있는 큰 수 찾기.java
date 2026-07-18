import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        
        for (int i = numbers.length-1; i >= 0; i--) {
            if (stack.isEmpty()) {
                answer[i] = -1;
                stack.push(numbers[i]);
            } else {
                // 자기보다 큰 게 나올때 까지 pop 시킴
                // stack 비면 -1 반환 후 자기자신 push
                while (!stack.isEmpty()) {
                    if (numbers[i] < stack.peek()) {
                        answer[i] = stack.peek();
                        break;
                    } else {
                        stack.pop();
                    }
                }
                if (stack.isEmpty()) {
                    answer[i] = -1;
                }
                stack.push(numbers[i]);
            }
        }
        
        return answer;
    }
}