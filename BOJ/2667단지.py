import sys
sys.setrecursionlimit(1000)

n = int(input())

graph = []
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

for i in range(n):
    graph.append(list(map(int, input())))
    
def dfs(x,y):
    global cnt
    
    if x < 0 or x >=n or y < 0 or y >= n:
        return 0
    
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
            
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i,j)
            result.append(cnt)
            cnt = 0

result.sort()

print(len(result))
for i in result:
    print(i)