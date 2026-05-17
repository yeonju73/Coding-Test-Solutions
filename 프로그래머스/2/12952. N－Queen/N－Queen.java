import java.util.*;

class Solution {
    int answer = 0;
    public int solution(int n) {
        
        // n번째 행에 있는 퀸의 자리
        int[] board = new int[n];
        backtracking(0, n, board);
        return answer;
    }
    // 수직, 대각선 검사
    public boolean isSafe(int row, int col, int[] board){
        for (int i = 0; i < row; i++) {
            if (board[i] == col){
                return false;
            }
            //row의 차이 = col의 차이라면 대각선으로 붙어있는 것
            if (Math.abs(row - i) == Math.abs(board[i] - col)) {
                return false;
            }
        }
        return true;
    }
    
    public void backtracking(int row, int n, int[] board){
        // 한 row 에 퀸 하나만 배치 -> row 순회
        // 성공했다면 count 올리고 반환
        if (row == n) {
            answer += 1;
            return;
        }
        
        for (int j = 0; j < n; j++) {
            boolean safe = isSafe(row, j+1, board);
            if (safe) {
                board[row] = j+1;
                backtracking(row+1, n, board);
                // 돌아오기
                board[row] = 0;
            }
        }
    }
}