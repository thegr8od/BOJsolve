

n,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(input()))

visited = [[False] *m for i in range(n)]


dx = [0,0,-1,1]
dy = [1,-1,0,0]
cnt = 0

def dfs(x,y):
    global cnt
    visited[x][y] = True
    if graph[x][y] == 'P':
        cnt += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n  and 0 <= ny < m:
            if graph[nx][ny] != 'X' and visited[nx][ny] == False:
                dfs(nx,ny)
             
for j in range(n):
    for k in range(m):
        if graph[j][k] == 'I':
            dfs(j,k)
        
if cnt != 0:
    print(cnt)
else:
    print('TT')