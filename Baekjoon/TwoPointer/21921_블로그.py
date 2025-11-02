import sys
input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
input_list = list(map(int, input().rstrip().split()))
sum_list = [0] * (n - x + 1)

for i in range(n):
    for j in range(x):
        index = i - j
        if 0 <= index < len(sum_list):
            sum_list[index] += input_list[i]

max_value = max(sum_list)
if max_value == 0:
    print("SAD")
else:
    count = 0
    for i in sum_list:
        if i == max_value:
            count += 1
    print(max_value)
    print(count)