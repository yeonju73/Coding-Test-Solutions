import sys
input = sys.stdin.readline

solved = False # 답 찾았는지 여부를 전역 상태로 관리

def dfs_recursion(graph:dict, v, visited:set, depth):
    global solved
    visited.add(v)
    depth += 1
    
    if depth == 5:
        solved = True
        return
    
    for node in graph[v]:
        if node not in visited:
            dfs_recursion(graph, node, visited, depth)
            visited.remove(node) # 백트래킹
    

def main():
    N, M = map(int, input().rstrip().split())
    relations = {i:[] for i in range(N)}

    for i in range(M):
        f1, f2 = map(int, input().rstrip().split())
        relations[f1].append(f2)
        relations[f2].append(f1)

    for i in range(N):
        if solved: 
            break
        visited = set()
        dfs_recursion(relations, i, visited, 0)
        
    print(1 if solved else 0)
        
main()