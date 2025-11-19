import sys
input = sys.stdin.readline

def backtracking(current_list:list):
    if len(current_list) == M:
        result_list.append(current_list.copy())
        return
    for i in range(1, N+1):
        if visited[i] :
            continue
        current_list.append(i)
        visited[i] = True
        backtracking(current_list)
        # 복구
        visited[i] = False
        current_list.pop()

N, M = map(int, input().rstrip().split())
result_list = list()
visited = {i:False for i in range(1, N+1)}
current_list = list()

backtracking(current_list)
    

for result in result_list:
    for r in result:
        print(r, end=' ')
    print()
