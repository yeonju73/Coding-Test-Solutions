import sys
input = sys.stdin.readline

n = int(input())
score_list = list()

for i in range(1, n+1):
    score_list.append(list(map(int, input().rstrip().split())))

visited = set()
min = -1

print(score_list)
