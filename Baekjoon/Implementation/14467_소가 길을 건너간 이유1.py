import sys
input = sys.stdin.readline

n = int(input().rstrip())
cow_dict = dict()
result_count = 0

for _ in range(n):
    cow_num, load = map(int, input().rstrip().split())
    
    if cow_num in cow_dict.keys():
        if cow_dict[cow_num] != load:
            result_count += 1
            cow_dict[cow_num] = load
    else:
        cow_dict[cow_num] = load
    
    
print(result_count)