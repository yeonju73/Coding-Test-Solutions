import sys
input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
input_list = list(map(int, input().rstrip().split()))

if max(input_list) == 0:
    print("SAD")
else: 
    # 슬라이딩 윈도우: 이전 구간의 합에서 맨 왼쪽 값은 빼고, 새로 들어온 맨 오른쪽 값은 더힘
    window_sum = sum(input_list[0:x])
    max_value = window_sum
    count = 1
    
    for i in range(x, n):
        window_sum = window_sum + input_list[i] - input_list[i - x]
        
        # 더 큰 값이 나오면 교체하고 count 초기화
        if max_value < window_sum:
            max_value = window_sum
            count = 1
        elif max_value == window_sum:
            count += 1
    
    print(max_value)
    print(count)