import sys
input = sys.stdin.readline

# 사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억
# 키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있었는지

# 키가 작은 사람부터 자리에 배치
# 아직 채워지지않은 빈칸으로 표시된 곳은 모두 나보다 키가 큰 사람이 들어갈 자리
# 0 0 1 0
# 0 2 1 0
# 0 2 1 3

n = int(input())
input_list = list(map(int, input().rstrip().split()))
result_list = list(0 for _ in range(n))

for i in range(n):
    
    # 나보다 키 큰 사람의 수
    count = 0
    r = 0

    while count < input_list[i]:
        if result_list[r] == 0:
            count += 1
        r += 1
    # 다른 사람(나보다 작은 사람)이 이미 서있는 자리는 넘김
    while r < n:
        if result_list[r] == 0:
            break
        r += 1

    result_list[r] = i + 1

print(*result_list)