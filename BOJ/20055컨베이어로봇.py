import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0]*n)
cnt = 0

while True:
    cnt += 1
    #회전 부분
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 #로봇 내리는 부분
    #먼저 올라온 로봇 부터 처리
    for i in range(n-2, -1,-1): #n-1은 로봇이 내리는 부분이라서, n-2부터
        if belt[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1
            robot[i] = 0
            belt[i + 1] -= 1
    robot[-1] = 0 #로봇 있으면 즉시 내린거임
    if belt[0] != 0 and robot[0] != 1: #올리는 위치에 내구도 0아니고 로봇이 없으면
        robot[0] = 1
        belt[0] -= 1
    if belt.count(0) >= k:
        break 
print(cnt)
