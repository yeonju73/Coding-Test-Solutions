import sys
input = sys.stdin.readline
# 로프1(10) - 로프2(15) 병렬
# 로프 중량의 최솟값 * 로프수k = 중량w의 물건을 들 수 있음

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)

# 지금 들 수 있는 최대 중량
result = 0
for i in range(N):
    # 지금 들 수 있는 최대 중량이, 새 로프를 걸었을 때의 최대 중량보다 작다면 업데이트
    # 끝까지 돌며 모든 경우의 수 확인
    result = max(result, ropes[i] * (i+1))
        
print(result)