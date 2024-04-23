graph = []

for _ in range(5):
    graph.append(list(map(str, input().split())))
    
ans = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(x,y,now):
    if len(now) == 6:
        if now not in ans:
            ans.append(now)
        return
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx,ny,graph[nx][ny]+now)
            
for i in range(5):
    for j in range(5):
        dfs(i,j,graph[i][j])
        
print(len(ans))