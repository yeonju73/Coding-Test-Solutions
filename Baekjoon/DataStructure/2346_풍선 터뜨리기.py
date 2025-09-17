import sys
input = sys.stdin.readline
output = sys.stdout
from collections import deque

n = int(input().rstrip())
list = list()
queue = deque((i, word) for i, word in enumerate(map(int, input().rstrip().split()), start=1))

for _ in range(n):
    popnum = queue.popleft()
    output.write(str(popnum[0]) + " ")
    if popnum[1] > 0:
        queue.rotate(popnum[1] - 1)
    else:
        queue.rotate(popnum[1] * -1)

output.write("\n")
output.flush()
output.close()
