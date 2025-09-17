import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
setList = set()
count = 0

for _ in range(n):
    setList.add(input().strip())

for _ in range(m):
    inputStr = input().strip()
    for setStr in setList:
        if inputStr == setStr:
            count += 1

print(count)
