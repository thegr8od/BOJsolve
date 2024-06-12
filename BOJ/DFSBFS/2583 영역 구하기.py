import sys
sys.setrecursionlimit(10**6)

m,n,k = map(int, input().split())

graph = []
for _ in range(k):
    graph.append(list(map(int, input().split())))
   
visited = [[False] * n for _ in range(m)]

for i in range(k):
    for k in range(m-graph[i][3],m-graph[i][1]):
        for j in range(graph[i][0], graph[i][2]):
            visited[k][j] = True
   
            
dx = [0,0,-1,1]
dy = [1,-1,0,0]

            
def dfs(x,y):
    global cnt
    cnt += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if visited[nx][ny] == False:
                dfs(nx,ny)
    return cnt

ans = []
num = 0
    
for i in range(m):
    for j in range(n):
        cnt = 0
        if visited[i][j] == False:
            ans.append(dfs(i,j))
            if cnt > 0:
                num += 1         

ans.sort()
print(num)          
print(*ans)                        
            
        