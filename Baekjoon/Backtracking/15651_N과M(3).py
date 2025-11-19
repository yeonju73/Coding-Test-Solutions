import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
numbers = [i for i in range(1, N+1)]

def backtracking(numbers:list):
    result = list()
    path = list()
    
    def dfs():
        if len(path) == M:
            result.append(path.copy())
            return
        for i in numbers:
            path.append(i)
            dfs()
            path.pop()
    dfs()
    return result

result_list = backtracking(numbers)
for result in result_list:
    print(*result)