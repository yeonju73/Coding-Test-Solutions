import sys
input = sys.stdin.readline

# 무게가 w일때 가질 수 있는 최대 가치 dp[w]
# dp[n] = max(dp[n-1], dp[n-2] + current_value)

n, k = map(int, input().rstrip().split())
dp = [0] * (k + 1)

# 무게가 6인 물건이 들어왔을 때
# dp[7] < d[1] + value 라면 업데이트
# dp[6] < dp[0] + value 라면? 업데이트

for _ in range(n):
    w, v = map(int, input().rstrip().split())
    # dp[j]가 이번 회차에 업데이트된 값을 참고하지 못하게 하려면,
    # 루프의 방향을 큰 것부터 내려와야 함
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(max(dp))
