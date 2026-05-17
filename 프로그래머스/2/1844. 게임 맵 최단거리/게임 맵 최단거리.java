import java.util.*;

class Solution {
    int answer = -1;
    int[] dx = {0, 0, 1, -1};
    int[] dy = {1, -1, 0, 0};
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        bfs(0, 0, maps, n, m);

        if (answer == Integer.MAX_VALUE) {
            answer = -1;
        }
        return answer;
    }
    
    public void bfs(int x, int y, int[][] maps, int n, int m) {
        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        
        queue.add(new int[]{x, y, 0});                                                                         
        visited[x][y] = true;
        
        while (!queue.isEmpty()){
            int[] node = queue.remove();
            
            if (node[0] == n-1 && node[1] == m-1) {
                answer = node[2]+1;
                return;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = node[0] + dx[i];
                int ny = node[1] + dy[i];

                if ((0 <= nx && nx < n) && (0 <= ny && ny < m)) {
                    if (maps[nx][ny] == 1 && !visited[nx][ny]) {
                        queue.add(new int[]{nx, ny, node[2]+1});
                        visited[nx][ny] = true;
                    }
                }
            }
        }
    }
}