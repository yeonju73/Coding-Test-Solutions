import sys
input = sys.stdin.readline

a_size, b_size = map(int, input().rstrip().split())
result_list = list()

a_pointer = 0
b_pointer = 0

a_list = list(map(int, input().rstrip().split()))
b_list = list(map(int, input().rstrip().split()))

while (a_pointer < a_size) and (b_pointer < b_size):
    if a_list[a_pointer] < b_list[b_pointer]:
        result_list.append(a_list[a_pointer])
        a_pointer += 1
    else:
        result_list.append(b_list[b_pointer])
        b_pointer += 1

if a_pointer < a_size:
    for i in range(a_pointer, a_size):
        result_list.append(a_list[i])
else:
    for i in range(b_pointer, b_size):
        result_list.append(b_list[i])
        
print(*result_list)