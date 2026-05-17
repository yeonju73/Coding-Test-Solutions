import java.util.*;

class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = 0;
        Arrays.sort(mats); // 오름차순 정렬
        
        int park_h = park[0].length;
        int park_r = park.length;
        System.out.println("park_h = " + park_h + ", park_r = " + park_r);
    
        for (int i = mats.length-1; i >= 0; i--) {
            int size = mats[i];
            
            for (int j = 0; j < park_r; j++) {
                for (int k = 0; k < park_h; k++) {
                    // 빈 칸이고 크기 가능이라면
                    if (park[j][k].equals("-1") && (j+size <= park_r) && (k+size <= park_h)) {
                        System.out.println("j = " + j + ", k = " + k);
                        
                        boolean flag = true;
                        for (int n = 0; n < size; n++) {
                            for (int m = 0; m < size; m++) {
                                if (!park[j+n][k+m].equals("-1")){
                                    flag = false;
                                    break;
                                }
                            }
                            if (!flag) break;
                        }
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