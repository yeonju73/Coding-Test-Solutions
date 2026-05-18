import java.util.*;

class Solution {
    public int solution(int[][] signals) {
        
        // 신호등이 몇개인지
        int signal_size = signals.length;
        ArrayList<ArrayList<Character>> sinal_array = new ArrayList<>(signal_size);
        
        for (int i = 0; i < signal_size; i++) {
            ArrayList<Character> temp = new ArrayList<>();
            
            for (int g = 0; g < signals[i][0]; g++) {
                temp.add('G');
            }
            for (int y = 0; y < signals[i][1]; y++) {
                temp.add('Y');
            }
            for (int r = 0; r < signals[i][2]; r++) {
                temp.add('R');
            }
            sinal_array.add(temp);
        }
        
        boolean flag = true;
        for (int time = 0; time < 2000000; time++) { 
            flag = true;
            
            for (int s = 0; s < signal_size; s++) {
                ArrayList<Character> curSignal = sinal_array.get(s);
                int curSize = curSignal.size();
                if (curSignal.get(time % curSize) != 'Y'){
                    flag = false;
                    break;
                }
            }
            if (flag) return time + 1;
        }
        return -1;
    }
}