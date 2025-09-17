import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
setList = set()
count = 0

for _ in range(n):
    setList.add(input().strip())
    
for _ in range(m):
    size = len(setList)
    inputStr = input().strip()
    setList.add(inputStr)
    if size == len(setList):
        count += 1
        continue
    setList.remove(inputStr)
    
print(count)
