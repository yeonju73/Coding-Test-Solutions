import java.util.*;
/**
    1번에서 가장 멀리 떨어진 노드가 몇개인지 리턴
    최단 경로로 이동했을 때 간선의 개수가 가장 많은 노드
    가중치가 없는 그래프 -> 간선 개수만 체크하면 됨
    map 으로 노드 연결 저장
    bfs로 풀면됨
**/
class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        Queue<int[]> queue = new ArrayDeque<>();
        
        // 각 노드로 가는 값 저장
        int[] distance = new int[n];
        Map<Integer, ArrayList<Integer>> map = new HashMap<>();
        
        boolean[] visited = new boolean[n];
        for(int i = 0; i < n; i++){
            map.put(i+1, new ArrayList<>());
        }
        for(int[] e: edge){
            map.get(e[0]).add(e[1]);
            map.get(e[1]).add(e[0]);
        }
        
        queue.offer(new int[]{1, 0});
        visited[0] = true;
        
        while(!queue.isEmpty()) {
            int[] node = queue.poll();
            int currentNode = node[0];
            int cost = node[1];
            
            distance[currentNode-1] = cost;
            
            for(int nextNode: map.get(currentNode)){
                if(!visited[nextNode-1]){
                    visited[nextNode-1] = true;
                    queue.offer(new int[]{nextNode, cost+1});
                }
            }
        }
        int maxValue = 0;
        for(int i = 1; i < n; i++){
            if(distance[i] > maxValue){
                maxValue = distance[i];
                answer=1;
            }
            else if(distance[i] == maxValue){
                answer++;
            }
        }
        
        return answer;
    }
    
}