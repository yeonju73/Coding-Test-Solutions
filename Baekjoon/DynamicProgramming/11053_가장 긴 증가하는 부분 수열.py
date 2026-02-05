import sys
input = sys.stdin.readline

n = int(input())
input_list = list(map(int, input().rstrip().split()))
# i번째 수까지 들어왔을때 가장 긴 증가하는 부분 수열의 최대 길이
# 1 1 1 1 1 1
# 1 2 1 1 1 1
# 1 2 1 1 1 1
# 1 2 1 
dp = [1] * n

for i in range(1, n):
    max_value = 1

    for j in range(i):
        if input_list[j] < input_list[i]:
            max_value = max(max_value, dp[j]+1)

    dp[i] = max_value

print(max(dp))