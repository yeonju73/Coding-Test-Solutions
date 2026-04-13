import sys
input = sys.stdin.readline

n = int(input())
score_list = list()

for _ in range(n):
    score_list.append(list(map(int, input().rstrip().split())))

# 한 팀만 구성해도 상대팀은 자동으로 구성됨
# 1은 무조건 포함한다고 가정하고 풀이
# 인원 중에서 N / 2 - 1 명 선택
visited = set()
visited.add(0)
min_value = 1e9

def dfs(index, count):
    global min_value
    if count == n // 2:
        start_team = 0
        link_team = 0

        # 팀 점수 계산
        for i in range(n):
            for j in range(n):
                if i in visited and j in visited:
                    start_team += score_list[i][j]
                elif i not in visited and j not in visited:
                    link_team += score_list[i][j]

        # 차이 최솟값 갱신
        # abs -> 절댓값
        min_value = min(abs(start_team - link_team), min_value)
        return
    
    for i in range(index, n):
        if i not in visited:
            visited.add(i)
            dfs(i + 1, count + 1)
            visited.remove(i) # 백트래킹

dfs(1, 1)
print(min_value)
