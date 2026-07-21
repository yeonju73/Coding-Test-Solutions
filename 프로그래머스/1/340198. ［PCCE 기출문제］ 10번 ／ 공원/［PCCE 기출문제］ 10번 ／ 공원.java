import java.util.*;

class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = 0;
        Arrays.sort(mats); // 오름차순 정렬
        
        int park_h = park[0].length;
        int park_r = park.length;
    
        for (int i = mats.length-1; i >= 0; i--) {
            int size = mats[i];
            
            for (int j = 0; j < park_r; j++) {
                for (int k = 0; k < park_h; k++) {
                    // 빈 칸이고 크기 가능이라면
                    if (park[j][k].equals("-1") && (j+size <= park_r) && (k+size <= park_h)) {
                        
                        boolean flag = true;
                        // 돗자리 크기 내에서 불가능 한 좌석 없는지 확인
                        for (int n = 0; n < size; n++) {
                            for (int m = 0; m < size; m++) {
                                // 비어있는 자리가 아니라면 flag 변경 후 break
                                if (!park[j+n][k+m].equals("-1")){
                                    flag = false;
                                    break;
                                }
                            }
                            if (!flag) break;
                        }
                        // 모든 땅 순회했을 때다 가능이었다면
                        if (flag) {
                            return size;
                        }
                    }
                }
            }
        }
        
        return -1;
    }
}