import sys
input = sys.stdin.readline

# nCr = (nPr / r!) = (n! /r!(n-r)!)
# nCn = 1, nC0 = 1

# dp[n] = n!
# nCr = dp[n] / dp[r] * dp[n-r]
dp = {0: 1, 1: 1}

N, M = map(int, input().rstrip().split())

for i in range(2, N+1):
    dp[i] = dp[i-1] * i
    
print(dp[N] // (dp[M] * dp[N-M]))