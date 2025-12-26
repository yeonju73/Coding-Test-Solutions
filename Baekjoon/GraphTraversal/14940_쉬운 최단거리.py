import sys
from collections import deque
input = sys.stdin.readline

# 세로, 가로
n, m = map(int, input().rstrip().split())

# 좌, 우, 상, 하
direc = ((0, -1), (0, 1), (-1, 0), (1, 0))

my_list = list()
# 거리 저장을 위한 배열 선언
dist = [[-1]*m for _ in range(n)]
start: tuple

for i in range(n):
    row = list(map(int, input().rstrip().split()))
    for j in range(m):
        if row[j] == 2:
            start = (i, j)
    my_list.append(row)


# bfs
queue = deque([start])
dist[start[0]][start[1]] = 0

while queue:
    current = queue.popleft()
    x, y = current[0], current[1]
        
    for dx, dy in direc:
        nx, ny = x + dx, y + dy
        # dist[nx][ny] == -1 구역을 방문 안 한 구역이라 생각
        if 0 <= nx < n and 0 <= ny < m and my_list[nx][ny] != 0 and dist[nx][ny] == -1:
            # 큐에 넣을 때 방문하고 값 업데이트
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))
                
for i in range(n):
    for j in range(m):
        if my_list[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()