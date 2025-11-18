T = int(input())
for test_case in range(1, T + 1):
    result = 0
    size = int(input())
    day_list = list(map(int, input().split()))
    max_value = max(day_list)
    max_index = day_list.index(max_value)
    
    spent_money = 0
    count = 0
    
    for i in range(size):
        if day_list[i] < max_value:
            spent_money += day_list[i]
            count += 1
        else: # max 를 만나면 팔고, 이후에 나오는 새로운 max 로 업데이트
            result += max_value * count - spent_money
            count = 0
            spent_money = 0
            # 마지막 값이 아니라면
            if i < size - 1:
                max_value = max(day_list[i+1:])
        
    print(f"#{test_case} {result}")