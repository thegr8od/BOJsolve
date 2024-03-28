#코드를 입력하세요.
import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0]*n)
cnt = 0

while True:
    cnt += 1
    #1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 #로봇이 있던 없던 내려서 무조건 0임
    
    #2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for i in range(n-2, -1,-1): #n-1은 로봇이 내리는 부분이라서, n-2부터
        if belt[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1
            robot[i] = 0
            belt[i + 1] -= 1
    robot[-1] = 0 #로봇 있으면 즉시 내린거임
    
    #3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if belt[0] != 0 and robot[0] != 1: #올리는 위치에 내구도 0아니고 로봇이 없으면
        robot[0] = 1
        belt[0] -= 1
        
    #4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다
    if belt.count(0) >= k:
        break 
print(cnt)
