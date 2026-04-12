import sys
sys.setrecursionlimit(3000)
input = sys.stdin.readline

direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().rstrip().split())
result = False
dot = list()

visited = set()
in_path = set()

def dfs(node, prev):
    global result
    if result: return
    print(node, "visited")
    
    visited.add(node)
    in_path.add(node)
    
    current_value = dot[node[0]][node[1]]
    
    for d in direc:
        dx = node[0]+d[0]
        dy = node[1]+d[1]
        # 현재 칸과 같은 색깔인 인접한 칸으로 이동
        if 0 <= dx < n and 0 <= dy < m and dot[dx][dy] == current_value:
                
            # 다음 이동할 칸이 이미 방문한 곳이라면 사이클이 생성됨
            # 바로 직전 위치가 원래 위치가 아니라면
            if (dx, dy) in in_path and prev != (dx, dy):
                result = True
                return
            
            if (dx, dy) not in visited:
                dfs((dx, dy), node)
            
    # 백트래킹 - 함수를 나갈 때 현재 노드 제거
    in_path.remove(node)

for i in range(n):
    dot.append(list(input().rstrip()))

for i in range(n):
    for j in range(m):
        if (i, j) not in visited:
            dfs((i, j), (i, j))
            
if (result == False):
    print("No")
else:
    print("Yes")