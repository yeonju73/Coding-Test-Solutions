import sys
input = sys.stdin.readline

n = int(input())
input_list = list(map(int, input().rstrip().split()))

# 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 
# 10, 6, 9, 10, 15, 21, -14, 12, 33, 32
# dp[i] = i번째 수를 반드시 포함하면서 끝나는 연속 부분합의 최대값
    # i에서 문제가 끝났을 때 답으로 할 값
# dp[i] = max(dp[i-1]+i, i)
dp = [input_list[0]]

for i in range(1, n):
    dp.append(max(dp[i-1] + input_list[i], input_list[i]))

print(dp)
print(max(dp))    
