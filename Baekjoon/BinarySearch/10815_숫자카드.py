import sys
input = sys.stdin.readline

n = int(input().rstrip())
my_card_list = sorted(list(map(int, input().rstrip().split())))

m = int(input().rstrip())
card_list = list(map(int, input().rstrip().split()))

result_list = [0] * m

for i in range(m):
    find_num = card_list[i]
    mid = n//2
    left = 0
    right = n - 1
    # print(f"find_num: {find_num}, mid: {mid}, left: {left}, right: {right}")

    while left <= right:
        if my_card_list[mid] == find_num:
            result_list[i] = 1
            break
        elif my_card_list[mid] < find_num:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
        # print(f"left: {left}, right: {right}, mid: {mid}")

# print(*result_list)            
print(' '.join(map(str, result_list))) 
