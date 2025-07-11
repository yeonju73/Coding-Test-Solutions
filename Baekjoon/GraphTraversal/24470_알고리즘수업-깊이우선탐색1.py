import sys

input = sys.stdin.readline

def dfs(graph, start, visited):
    count = 1
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if visited[node] == 0:
            visited[node] = count
            count += 1
            
        print(stack)
        for next in graph[node]:
            if visited[next] == 0:
                stack.append(next)
                print(stack)
                
    print(visited)

def main():
    n, m, r = map(int, input().split())
    graph = {i: [] for i in range(1, n+1)}
    visited = {i: 0 for i in range(1, n+1)}
    
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x) # 양방향 그래프
    print(graph)
    
    for j in range(1, n+1):
        graph[j].sort(reverse=True)
        
    print(graph)
    dfs(graph, r, visited)
    
    for i in visited.values():
        print(i)
    
main()