import sys
from collections import deque
input = sys.stdin.readline

# 세로, 가로
n, m = map(int, input().rstrip().split())

# 좌, 우, 상, 하
direc = ((0, -1), (0, 1), (-1, 0), (1, 0))

my_list = list()
start: tuple

for i in range(n):
    input_list = list(map(int, input().rstrip().split()))
    if 2 in input_list:
        start = (i, input_list.index(2))
    my_list.append(input_list)


# bfs
my_list[start[0]][start[1]] = 0
queue = deque([start])


while queue:
    current = queue.popleft()
    value = my_list[current[0]][current[1]]
    
    for d in direc:
        dx = current[0] + d[0]
        dy = current[1] + d[1]
        
        # 1일 때 아직 방문 하지 않은 노드라 판별
        if 0 <= dx < n and 0 <= dy < m and my_list[dx][dy] == 1:
            my_list[dx][dy] = value + 1 # 거리 갱신
            queue.append((dx, dy)) # 큐에 넣고
            visited.add((dx, dy)) # 방문처리
                
for line in range(n):
    for i in range(m):
        if my_list[line][i] == 1 and (line, i) not in visited:
            print(-1, end=' ')
        else:
            print(my_list[line][i], end=' ')
    print()