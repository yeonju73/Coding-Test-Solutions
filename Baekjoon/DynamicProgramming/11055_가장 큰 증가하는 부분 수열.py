import sys
input = sys.stdin.readline

n = int(input())
input_list = list(map(int, input().rstrip().split()))

# dp[n] = n까지 일때 가장 큰 증가하는 부분 수열의 합
dp = input_list[:] # 자기자신의 값으로 초기화

for i in range(1, n):
    # 이전 값 중에 input[n-1] 값이 n보다 작다면, dp[n-1] + n 한 것들 중에 최대가 dp[n]
    max_value = input_list[i]

    for j in range(i):
        if input_list[j] < input_list[i]:
            max_value = max((dp[j] + input_list[i]), max_value)
    
    dp[i] = max_value

print(max(dp))