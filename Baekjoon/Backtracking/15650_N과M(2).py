import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
numbers = [i for i in range(1, N+1)]

def backtracking(numbers:list):
    result = list()
    visited = {i: False for i in range(1, N+1)}
    path = list()
    
    def dfs():
        # 종료 조건
        if len(path) == M:
            result.append(path.copy())
            return
        # 가능한 모든 조건 탐색
        for i in numbers:
            if visited[i] == False and (len(path) < 1 or path[-1] < i):
                visited[i] = True
                path.append(i)
                dfs()
                # 복구
                path.pop()
                visited[i] = False
    dfs()
    return result

result = backtracking(numbers)
for r in result:
    print(*r)