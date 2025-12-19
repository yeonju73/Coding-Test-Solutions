import sys
input = sys.stdin.readline

def dfs_recursion(graph:dict, v, visited:set, depth):
    visited.add(v)
    depth += 1
    
    if depth == 5:
        print(1)
        exit()
    
    for node in graph[v]:
        if node not in visited:
            dfs_recursion(graph, node, visited, depth)
            visited.remove(node)
    

def main():
    N, M = map(int, input().rstrip().split())
    relations = {i:[] for i in range(N)}

    for i in range(M):
        f1, f2 = map(int, input().rstrip().split())
        relations[f1].append(f2)
        relations[f2].append(f1)

    for i in range(N):
        visited = set()
        dfs_recursion(relations, i, visited, 0)
        
    print(0)
        
main()