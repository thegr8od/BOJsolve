n = int(input())

graph = []
visited = [[0] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
idx = 0
    
def dfs(x,y,now):
    global idx
    visited[x][y] = 1
    if now == -1:
        idx += 1
        return
    nx = x + now
    ny = y + now
    if 0 <= nx < n:
        if visited[nx][y] == 0:
            dfs(nx,y,graph[nx][y])
    if 0 <= ny < n:
        if visited[x][ny] == 0:
            dfs(x,ny,graph[x][ny])

dfs(0,0,graph[0][0])

if idx == 0:
    print('Hing')
else:
    print('HaruHaru')        
        