import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
    exit()
    
# dp[i] = 2 * i 사이즈일때 방법의 수
dp = [0] * (N + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    # 점화식
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N] % 10007)