import sys
input = sys.stdin.readline

n = int(input())
file_dic = dict()

for _ in range(n):
    file, ext = input().rstrip().split(".")
    if ext in file_dic.keys():
        file_dic[ext] += 1
    else:
        file_dic[ext] = 1

for k, v in sorted(file_dic.items()):
    print(f"{k} {v}")