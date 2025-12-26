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
queue = deque(list())
visited = set()
queue.append((start[0], start[1], 0))

while queue:
    current = queue.popleft()
    current_point = (current[0], current[1])
    
    if current_point not in visited:
        visited.add(current_point)
        
        # 처음 방문일 때만 값 업데이트
        value = current[2]
        my_list[current_point[0]][current_point[1]] = value
        
        for d in direc:
            dx = current_point[0] + d[0]
            dy = current_point[1] + d[1]
            
            if 0 <= dx < n and 0 <= dy < m and my_list[dx][dy] != 0:
                queue.append((dx, dy, value+1))
                
for line in range(n):
    for i in range(m):
        if my_list[line][i] == 1 and (line, i) not in visited:
            print(-1, end=' ')
        else:
            print(my_list[line][i], end=' ')
    print()