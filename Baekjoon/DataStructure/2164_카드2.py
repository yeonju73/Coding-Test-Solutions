# pop 2번하고 두번째 pop 한 거 맨 뒤에 추가
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

queue = deque([i for i in range(1, n+1)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
    print(queue)

print(queue.pop())
