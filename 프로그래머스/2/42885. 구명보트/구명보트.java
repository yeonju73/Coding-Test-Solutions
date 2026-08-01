import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        // 배열을 오름차순 정렬
        Arrays.sort(people);
        
        // 왼, 오 포인터 중앙으로 이동
        // 오른쪽 사람을 태운 후, 왼쪽 사람도 태울 수 있다면 태움
        // 태웠다면 포인터 이동
        // 태우지 못했다면 오른쪽만 태움
        // 두 포인터가 만날때 까지 반복
        int left = 0;
        int right = people.length -1;
        
        while(right >= left) {
            // 중간지점에서 만났을 때
            if(right == left){
                answer++;
                break;
            }
                
            if(people[right] + people[left] <= limit){
                left++;
                right--;
            } else{
                right--;
            }
            answer++;
        }
        
        return answer;
    }
}