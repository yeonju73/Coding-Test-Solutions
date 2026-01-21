import sys
from collections import deque
input = sys.stdin.readline

node = int(input())
edge = int(input())
edge_list = {i:[] for i in range(1, node+1)}

for i in range(edge):
    first, second = map(int, input().rstrip().split())
    edge_list[first].append(second)
    edge_list[second].append(first)

# bfs
queue = deque([1])
visit = [1]

while queue:
    next = queue.popleft()
    for nextnode in edge_list[next]:
        if nextnode not in visit:
            queue.append(nextnode)
            visit.append(nextnode)
            
print(len(visit) - 1) # 1번 컴퓨터는 제외