from collections import deque
import sys
input = sys.stdin.readline

n,m,x,k = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [0] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    
def bfs(start):
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    ans.append(i)
ans = []
ans.sort()
bfs(x)

if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)
