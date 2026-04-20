import sys
input = sys.stdin.readline

# 현재 집을 빨/파/초로 칠했을 때의 각각의 최솟값
# dp[n][빨] = n번째 집을 빨간색으로 칠하는 비용 + min(dp[n-1][초], dp[n-1][파])
dp = list()

n = int(input())
input_list = list()
for i in range(n):
    input_list.append(list(map(int, input().rstrip().split())))

for house in input_list:
    if len(dp) == 0:
        dp.append(house)
        continue
    
    house_list = list()
    house_list.append(house[0] + min(dp[-1][1], dp[-1][2]))
    house_list.append(house[1] + min(dp[-1][0], dp[-1][2]))
    house_list.append(house[2] + min(dp[-1][0], dp[-1][1]))
            
    dp.append(house_list)
    
print(min(dp[-1]))