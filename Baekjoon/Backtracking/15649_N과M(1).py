import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

def solve():
    numbers = [i for i in range(1, N+1)]
    result_list = backtracking_permutations(numbers, M)
    for result in result_list:
        print(*result) # 리스트 안의 값을 공백으로 자동 구분해서 출력

def backtracking_permutations(nums, size):
    result = []
    visited = [False] * len(nums)
    path = []
    
    def dfs():
        # 종료 조건
        if len(path) == size:
            result.append(path.copy())
            return
        
        # 모든 후보 탐색
        for i in range(len(nums)):
            if visited[i]:
                continue
            # 선택 (go down)
            visited[i] = True
            path.append(i+1)
            
            # 재귀호출
            dfs()
            
            # 되돌리기
            visited[i] = False
            path.pop()
    
    dfs()
    return result

solve()