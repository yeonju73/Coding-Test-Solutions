import sys
input = sys.stdin.readline
# 같은 원소가 K개 이하로 들어 있는 최장 연속 부분 수열
n, m = map(int, input().rstrip().split())
my_list = list(map(int, input().rstrip().split()))

my_dict = dict()

result = 0
right = 0
left = 0

while left >= 0 and right < n:
    
    value = my_list[right]
    
    if value not in my_dict.keys():
        my_dict[value] = 1
    else:
        # 이미 꽉 차있는 수가 더 들어오면
        # left를 오른쪽으로 옮겨가며 범위줄여나가기
        if my_dict.get(value) == m:
            
            while my_dict.get(value) == m:
                my_dict[my_list[left]] -= 1
                left += 1
            # 이 loop를 빠져나오면 m 보다 작아짐
                
        my_dict[value] += 1
    # 길이의 최댓값 저장
    result = max(right-left+1, result)
    right += 1
    
print(result)