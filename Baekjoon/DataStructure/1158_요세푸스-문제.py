import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

myQueue = deque([i for i in range(n, 0, -1)])

sys.stdout.write("<")
for _ in range(n - 1):
    myQueue.rotate(k)
    sys.stdout.write(str(myQueue.popleft()) + ", ")
sys.stdout.write(str(myQueue.popleft()) + ">\n")

sys.stdout.flush()
sys.stdout.close()