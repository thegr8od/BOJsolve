import sys
sys.setrecursionlimit(10**6)

m,n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int,input())))
    


dx = [1,-1,0,0]
dy = [0,0,-1,1]


cnt = 0

def dfs(x,y):
    global cnt
    graph[x][y] = 1
    if x == (m-1):
        cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <m and 0<= ny <n:
                if graph[nx][ny] == 0:
                    dfs(nx,ny)

for j in range(n):
    if graph[0][j] == 0:
        dfs(0,j)
        
if cnt == 0:
    print("NO")
else:
    print("YES")  
    