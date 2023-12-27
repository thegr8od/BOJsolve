import sys
input = sys.stdin.readline
from collections import deque

queue = deque()
N = int(input())

for i in range(N):
    command = input().split()
    if command[0] == "push_front":
        queue.appendleft(command[1])
    elif command[0] == "push_back":
        queue.append(command[1])
    elif command[0] == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0]) 
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

   


