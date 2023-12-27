import sys
input = sys.stdin.readline
from collections import deque

queue = deque()
N = int(input())

for i in range(1,N+1):
    queue.append(i)


while len(queue) >=2:
    queue.popleft()
    queue.append(queue.popleft())


print(*queue)
