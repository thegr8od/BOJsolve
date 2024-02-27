from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(q):
    cnt = 0
    queue = deque(q)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny <0 or nx >=n or ny >=m:
                continue
            if graph[nx][ny] != 0:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    for i in graph:
        if 0 in i:
            cnt += 1
    
    if cnt != 0:
        return -1
    else:
        return max(map(max, graph))


x = 0
y = 0 

q = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

answer = bfs(q)

if answer != -1:
    print(bfs(q)-1)
else:
    print(-1)
