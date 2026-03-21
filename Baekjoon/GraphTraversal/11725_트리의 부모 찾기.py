import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = {i:[] for i in range(1, n+1)}

for _ in range(n-1):
    start, end = map(int, input().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)

result = {i:1 for i in range(2, n+1)}

# BFS
# 1번 루트 노드부터 너비우선 탐색을 하면서 바로 직전 노드를 부모로 저장
start = 1
queue = deque([start])
visited = set([start])

while queue:
    current = queue.popleft() # 맨 앞에서 빼오기
    
    for next in graph.get(current):
        if next not in visited:
            queue.append(next)
            visited.add(next)
            result[next] = current

for k, v in result.items():
    print(v)