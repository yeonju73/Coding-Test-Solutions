import java.util.*;

// 1. 매 요청마다 (0,0)에서 BFS를 돌려 '현재 외부와 연결된 빈칸'을 찾는다 (boolean[][] isAccessible)
// 2. 지게차(len 1): storage[i][j] == alpha 이고 주변에 isAccessible인 칸이 하나라도 있으면 제거
// 3. 크레인(len 2): storage[i][j] == alpha 이면 무조건 제거

class Solution {
    int[] dx = {0, 0, 1, -1};
    int[] dy = {1, -1, 0, 0};
    int answer = 0;
    
    public int solution(String[] storage, String[] requests) {
        int n = storage.length;
        int m = storage[0].length();
        
        boolean[][] isAvailable = new boolean[n+2][m+2];
        
        // 외곽 패딩을 1 넣은 배열
        char[][] map = new char[n+2][m+2];
        
        for (int i = 0; i < n+2; i++) {
            for (int j = 0; j < m+2; j++) {
                if (j == 0 || j == m+1 || i == 0 || i == n+1) {
                    map[i][j] = '.';
                } else {
                    map[i][j] = storage[i-1].charAt(j-1);
                }
            }
        }
        
        for (String req: requests) {
            
            Set<int[]> toRemove = new HashSet<>();
            
            if (req.length() > 1) {
                for (int i = 0; i < n+2; i++){
                    for (int j = 0; j < m+2; j++){
                        // 알파벳이 같을 경우
                        if (map[i][j] == req.charAt(0)){
                            toRemove.add(new int[]{i, j});
                        }
                    }
                }
            }
            else {
                isAvailable = bfs(map, n, m);
                
                for (int i = 0; i < n+2; i++){
                    for (int j = 0; j < m+2; j++){
                        // 알파벳이 같고 외부에서 접근 가능하다면
                        if (map[i][j] == req.charAt(0)){
                            for (int k=0; k < 4; k++) {
                                int nx = i + dx[k];
                                int ny = j + dy[k];
                                if ((nx >= 0 && nx < n+2) && (ny >= 0 && ny < m+2) && isAvailable[nx][ny]){
                                    toRemove.add(new int[]{i, j});
                                }
                            }
                        }
                    }
                }
            }
            for (int[] tr: toRemove) {
                map[tr[0]][tr[1]] = '.';
            }
        }
        
        answer = (int) Arrays.stream(map)
            .flatMapToInt(row -> new String(row).chars())
            .filter(c -> c != '.')
            .count();
        
        return answer;
    }
    
    public boolean[][] bfs(char[][] map, int n, int m) {
        boolean[][] visited = new boolean[n+2][m+2];
        Queue<int[]> queue = new ArrayDeque<>();
        
        visited[0][0] = true;
        queue.add(new int[]{0, 0});
        
        while(!queue.isEmpty()) {
            int[] node = queue.poll();
            
            for (int k=0; k < 4; k++) {
                int nx = node[0] + dx[k];
                int ny = node[1] + dy[k];
                // 외부에서 접근 가능하고 방문한 적 없다면 queue에 추가
                if ((nx >= 0 && nx < n+2) && (ny >= 0 && ny < m+2) && !visited[nx][ny] && map[nx][ny] == '.'){
                    visited[nx][ny] = true;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
        return visited;
    }
    
}