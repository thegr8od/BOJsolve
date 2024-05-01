from collections import deque

n, m = map(int, input().split())

dx = [1,1,1,0,-1,-1,-1,0,1]
dy = [-1,0,1,1,1,0,-1,-1,-1]

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()

max_value = 0
    
def bfs():
    global max_value
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x +dx[i]
            ny = y +dy[i]
            if nx < 0 or nx >= n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                max_value = graph[nx][ny]
                queue.append((nx,ny))
            
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            queue.append((i,j))

bfs()

print(max_value - 1)