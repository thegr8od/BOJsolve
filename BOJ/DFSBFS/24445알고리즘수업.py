import sys
input = sys.stdin.readline

from collections import deque

n,m,r = map(int, input().split())

visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort(reverse=True)
    
cnt = 1
def bfs(start):
    global cnt
    queue = deque([start])
    visited[start] = cnt 
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                cnt += 1
                queue.append(i)
                visited[i] = cnt
bfs(r)
for j in range(1,n+1):
    print(visited[j])