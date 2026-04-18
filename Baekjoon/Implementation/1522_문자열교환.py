import sys
input = sys.stdin.readline

input_string = input().rstrip()

# 특정 구간 안에 포함된 b의 개수 = 필요한 교환 횟수
a_count = input_string.count('a')
        
# 슬라이딩 윈도우
# a의 총 개수인 길이만큼 가능한 모든 구간을 탐색
# b의 개수가 가장 적은 구간 -> 교환을 가장 적게해도 됨

input_list = [s for s in input_string]

# 원형 문자열 처리
# 문자열을 두 번 이어붙여서 길이를 두 배로 늘림
# input_list = input_list + input_list[:a_count]

min_value = 1e9

for i in range(len(input_list)):
    last = (i+a_count) % len(input_list)
    # 이어붙였을 경우: len(input_list) - a_count 까지만 for문을 돈다.
    # min_value = min(min_value, input_list[i:last].count('b'))
    
    b_count = 0
    if last < i:
        b_count += input_list[:last].count('b')
        b_count += input_list[i:].count('b')
    else:
        b_count += input_list[i:last].count('b')
    
    if b_count == 0:
        min_value = b_count
        break
    
    min_value = min(min_value, b_count)
    
print(min_value)