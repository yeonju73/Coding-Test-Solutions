import sys
input = sys.stdin.readline

n = int(input())

# 1. 5원을 최대한 많이 사용
count = n // 5
remainder = n % 5

# 5원 개수를 하나씩 줄여가며, 남은 돈이 2원으로 나누어 떨어지는 지 확인
while count >= 0:
    if remainder % 2 == 0:
        count += (remainder // 2)
        break
    # 2로 나누어 떨어지지 않으면 5원 하나 반납
    count -= 1
    remainder += 5

print(count)