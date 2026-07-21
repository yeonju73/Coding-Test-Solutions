class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        // 마지막으로 칠한 인덱스
        // lastPainting 이하로는 모두 색칠된 것 보장됨
        int lastPainting = 0; 
        
        for (int s : section){
            // 지금 칠해야 할 곳이 마지막으로 칠한 곳 보다 이후라면 덧칠해야함
            if (s > lastPainting) {
                // 마지막으로 칠해진 인덱스: 시작점 + 롤러의 길이 - 1
                lastPainting = s + m - 1;
                answer++;
            }
        }
        
        return answer;
    }
}