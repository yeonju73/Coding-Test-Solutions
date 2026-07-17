import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        
        int n = maps.length;
        int m = maps[0].length;
        
        int[][] visited = new int[n][m];
        
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        Queue<int[]> queue = new ArrayDeque<>();
        
        queue.offer(new int[]{0, 0});
        visited[0][0] = 1;
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            
            int i = current[0];
            int j = current[1];
        
            if (i == n-1 && j == m-1) {
                break;
            }
            for (int d = 0; d < 4; d++) {
                int nextX = i + dx[d];
                int nextY = j + dy[d];

                if(nextX >= 0 && nextX < n && nextY >= 0 && nextY < m && (maps[nextX][nextY] == 1) && (visited[nextX][nextY] == 0)){
                    queue.offer(new int[]{nextX, nextY});
                    visited[nextX][nextY] = visited[i][j]+1;
                }
            }
        }
        
        if (visited[n-1][m-1] == 0) return -1;
        return visited[n-1][m-1];
    }
}