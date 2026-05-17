import java.util.*;

class Solution {
    public int solution(String s) {
        if (s.length() == 1) {
            return 1;
        }
        
        int answer = s.length();
                
        // size = 압축할 크기
        for (int size  = 1; size <= s.length() / 2 ; size++) {
            StringBuilder sb = new StringBuilder();
             
            int count = 1;
            // 처음 비교 기준이 될 string 추출
            String target = s.substring(0, size);
            
            // size 만큼 인덱스를 건너뛰며 비교
            for (int i = size; i < s.length(); i += size) {
                
                // 2 4 6
                // 남은 문자열이 size 보다 작으면 끝까지 자름
                String next;
                if (s.length() - i < size) {
                    next = s.substring(i, s.length());
                } else {
                    next = s.substring(i, i+size);
                }
                
                // 연속으로 같으면 카운트 증가
                if (target.equals(next)) {
                    count++;
                } else {
                    // 다르면 지금까지의 결과를 압축된 문자열에 추가
                    if (count > 1) { // 1일땐 생략
                        sb.append(count);
                        count = 1;
                    }
                    sb.append(target);
                }
                
                // 비교 기준을 현재 string 으로 갱신
                target = next;
            }
            // 남은 값 붙여넣기
            if (count > 1) {
                sb.append(count);
                count = 1;
            }
            sb.append(target);
            
            // min 값 업데이트
            answer = Math.min(answer, sb.length());
        }
        return answer;
    }
}