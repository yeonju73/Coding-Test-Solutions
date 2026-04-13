import sys
input = sys.stdin.readline

n = 19
board = list()
# 우, 하, 대각선 아래 우, 대각선 위 우
direction = [(0, 1), (1, 0), (1, 1), (-1, 1)]

# 가로, 세로, 대각선으로 5개 같은 색이 있으면 이김
# 6알 이상이 연속적으로 놓이면 이긴것이 아님

# 검은색 또는 흰색이 이겼을 경우
# 연속된 다섯 개의 바둑알 중에서 가장 왼쪽에 있는 바둑알
# (연속된 다섯 개의 바둑알이 세로로 놓인 경우,그 중 가장 위에 있는 것)
# 의 가로줄 번호와, 세로줄 번호를 순서대로 출력

for i in range(n):
    board.append(list(map(int, input().rstrip().split())))

flag = False
for i in range(n):
    if flag:
        break

    for j in range(n):
        if flag:
            break
        if board[i][j] != 0:
            value = board[i][j]
            # 각 방향별로 5개 연속해서 존재하는 지 확인
            for d in direction:
                # 이 방향에서 성공한다 가정
                flag = True
                for m in range(1, 5):
                    dx = i + (d[0] * m)
                    dy = j + (d[1] * m)
                    if 0 <= dx < n and 0 <= dy < n and board[dx][dy] == value:
                        continue
                    else: 
                        # 실패했을 시 플레그 변경
                        flag = False
                        break
                # 이 방향에서 성공했을 경우 육목인지 판정
                if flag:
                    dx_up = i + (d[0] * 5)
                    dy_up = j + (d[1] * 5)
                    dx_down = i + (d[0] * -1)
                    dy_down = j + (d[1] * -1)
                    if 0 <= dx_up < n and 0 <= dy_up < n and board[dx_up][dy_up] == value:
                        flag = False
                    if 0 <= dx_down < n and 0 <= dy_down < n and board[dx_down][dy_down] == value:
                        flag = False

                # 육목 검사 후에도 true면 
                if flag:
                    print(board[i][j])
                    print(i+1, j+1)
                    break

if not flag:
    print(0)
