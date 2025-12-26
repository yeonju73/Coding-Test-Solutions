import sys
input = sys.stdin.readline

n = int(input())
schedules = [0] * 365

for _ in range(n):
    start, end = map(int, input().rstrip().split())
    for d in range(start - 1, end):
        schedules[d] += 1

result = 0
width = 0
height = 0

for sche in schedules:
    if sche > 0:
        width += 1
        height = max(height, sche)
    else:
        result += (width * height)
        width, height = 0, 0
            
result += (width * height)
print(result)