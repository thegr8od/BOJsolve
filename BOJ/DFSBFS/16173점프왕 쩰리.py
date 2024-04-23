import sys
sys.setrecursionlimit(10**6)

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
idx = 0
    
def dfs(x,y,now):
    global idx
    if now == -1:
        idx += 1
        return
    nx = x + now
    ny = y + now
    if 0 <= nx < n:
        dfs(nx,y,graph[nx][y])
    if 0 <= ny < n:
        dfs(x,ny,graph[x][ny])

dfs(0,0,graph[0][0])

if idx == 0:
    print('Hing')
else:
    print('HaruHaru')        
        