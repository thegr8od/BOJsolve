from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# BFS 메서드 정의
def bfs(x,y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    return graph[n-1][m-1]

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = []

visited = [False] * 9

n, m = map(int, input().split())
for i in range(n):
    graph.append(list(map(int, input())))

print(bfs(0,0))
