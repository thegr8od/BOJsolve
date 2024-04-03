import sys
sys.setrecursionlimit(100000)


n = int(input())
graph = []
max_num = 0
result = 1

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    
    for j in data:
        if j > max_num:
            max_num = j

def dfs(x,y,limit):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
            if graph[nx][ny] > limit:
                visited[nx][ny] = 1
                dfs(nx,ny,limit)
                
for i in range(max_num):
    visited = [[0] *n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                cnt += 1
                visited[j][k] =1
                dfs(j,k,i)
    result = max(result, cnt)

print(result)    