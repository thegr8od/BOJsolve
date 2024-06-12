import sys
sys.setrecursionlimit(10**6)

t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx <h and 0<= ny < w and visited[nx][ny] == False:
            if data[nx][ny] == '#':
                dfs(nx,ny)
    return True

            
for _ in range(t):
    h,w = map(int, input().split())
    cnt = 0
    visited = [[False] * w for _ in range(h)]
    data = []
    for i in range(h):
        data.append(list(input()))
        
    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and data[i][j] == '#':
                if dfs(i,j) == True:
                    cnt += 1
    print(cnt)

            