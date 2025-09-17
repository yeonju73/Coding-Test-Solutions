import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
setList = set()
count = 0

for _ in range(n):
    setList.add(input().strip())
    
for _ in range(m):
    if input().strip() in setList:
        count += 1
    
print(count)
