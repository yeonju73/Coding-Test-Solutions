import sys
import copy
input = sys.stdin.readline

# 50년이 지나면, 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨버린다
# 지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형이다.
R, C = map(int, input().rstrip().split())
my_list = list()
new_list = list()

for i in range(R):
    my_list.append(list(input().rstrip()))

new_list = copy.deepcopy(my_list)

startR = R
endR = 0
startC = C
endC = 0

for i in range(R):
    for j in range(C):
        if my_list[i][j] == '.':
            continue
        if my_list[i][j] == 'X':
            # 상하좌우 중 . 또는 범위를 넘어가는 곳이 3곳 이상인가
            count = 0
            if i-1 < 0 or my_list[i-1][j] == '.':
                count += 1
            if j-1 < 0 or my_list[i][j-1] == '.':
                count += 1
            if i+1 >= R or my_list[i+1][j] == '.':
                count += 1
            if j+1 >= C or my_list[i][j+1] == '.':
                count += 1
            
            if count >= 3:
                new_list[i][j] = '.'
            else:
                new_list[i][j] = 'X'
                startR = min(startR, i)
                startC = min(startC, j)
                endR = max(endR, i+1)
                endC = max(endC, j+1)
                
for i in range(startR, endR):
    for j in range(startC, endC):
        print(new_list[i][j], end="")
    print()
