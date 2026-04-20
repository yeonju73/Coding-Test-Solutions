import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
input_list = list()
for i in range(n):
    input_list.append(list(input().rstrip()))
    
direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = set()
rg_visited = set()

def rg_dfs(node, b_value):
    rg_visited.add(node)
    
    for d in direc:
        dx = node[0] + d[0]
        dy = node[1] + d[1]
        
        if 0 <= dx < n and 0 <= dy < n:
            if (b_value and input_list[dx][dy] == 'B') or ((not b_value) and (input_list[dx][dy] != 'B')):
                if (dx, dy) not in rg_visited:
                    rg_dfs((dx, dy), b_value)
    
    
def dfs(node, value):
    visited.add(node)
    
    for d in direc:
        dx = node[0] + d[0]
        dy = node[1] + d[1]
        
        if 0 <= dx < n and 0 <= dy < n and input_list[dx][dy] == value:
            if (dx, dy) not in visited:
                dfs((dx, dy), value)
                
count = 0   
for i in range(n):
    for j in range(n):
        if (i, j) not in visited:
            dfs((i, j), input_list[i][j])
            count += 1

rg_count = 0   
for i in range(n):
    for j in range(n):
        if (i, j) not in rg_visited:
            if input_list[i][j]=='B':
                rg_dfs((i, j), True)
            else: rg_dfs((i, j), False)
            rg_count += 1

print(count, rg_count)