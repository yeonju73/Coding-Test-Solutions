import java.util.*;

class Solution {
    class Node implements Comparable<Node> {
        int number;
        int distance;
        
        public Node(int number, int distance) {
            this.number = number;
            this.distance = distance;
        }
        
        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.distance, other.distance);
        }
    }
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;
        
        // 최단 거리 배열
        int[] distS = new int[n]; 
        int[] distA = new int[n];
        int[] distB = new int[n];
        
        Arrays.fill(distS, Integer.MAX_VALUE);
        Arrays.fill(distA, Integer.MAX_VALUE);
        Arrays.fill(distB, Integer.MAX_VALUE);
        
        // node별 연결된 간선 저장
        ArrayList<ArrayList<Node>> graph = new ArrayList<>();
        
        for(int i = 0; i < n; i++){
            graph.add(new ArrayList<>());
        }
        
        // 그래프 초기화
        for(int[] f : fares){
            graph.get(f[0]-1).add(new Node(f[1]-1, f[2]));
            graph.get(f[1]-1).add(new Node(f[0]-1, f[2]));
        }
        
        dijkstra(s-1, graph, distS);
        dijkstra(a-1, graph, distA);
        dijkstra(b-1, graph, distB);
        
        // 모든 노드를 합승 중단 지점 X로 하여
        // start->X  + X->A + X->B 값이 최소인거
        for(int i = 0; i < n; i++) {
            if((distS[i] != Integer.MAX_VALUE) && (distA[i] != Integer.MAX_VALUE)&& (distB[i] != Integer.MAX_VALUE)){
                int cost = distS[i] + distA[i] + distB[i];
                answer = Math.min(cost, answer);
            }
        }
        
        return answer;
    }
    
    public void dijkstra(int start, ArrayList<ArrayList<Node>> graph, int[] dist) {
        Queue<Node> pq = new PriorityQueue<>();
        
        // 시작 노드 insert
        pq.offer(new Node(start, 0));
        // 시작지점까지의 최단 거리는 0
        dist[start] = 0;
        
        while(!pq.isEmpty()) {
            
            Node node = pq.poll();
            int number = node.number;
            int distance  = node.distance;
            
            if(dist[number] < distance) continue;
            
            // node 연결되어있는 거를 순회
            // 걔를 거쳐가는게 더 이득인지 판단!!
            for(Node n : graph.get(number)){
                // dist[number]: 현재 노드까지 가는 최단 거리
                // n.distance: 현재 노드에서 인접 노드까지 가는 거리
                int cost = dist[number] + n.distance;
                // 인접 노드로 가는 최단 거리 갱신
                // 현재 노드를 거쳐서 가는 것이 더 최단이라면
                // dist[n.number]: 지금 저장된 n번 노드로 가는 최단거리
                if (cost < dist[n.number]){
                    dist[n.number] = cost;
                    // 값이 변경된게 있으면 큐에 넣어서 인접된 노드까지 최단 거리 변경이 있는지 확인
                    pq.offer(new Node(n.number, dist[n.number]));
                }
            }
            
        }
        
        
        
    }
}