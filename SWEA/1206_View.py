for test_case in range(1, 11):
    result = 0
    size = int(input())
    my_list = list(map(int, input().split()))
    for i in range(2, size-2) :
        if my_list[i-2] >= my_list[i] or my_list[i-1] >= my_list[i] or my_list[i+1] >= my_list[i] or my_list[i+2] >= my_list[i] :
            continue
        result = result + my_list[i] - max(my_list[i-2], my_list[i-1], my_list[i+1], my_list[i+2])
        
    print(f"#{test_case} {result}")