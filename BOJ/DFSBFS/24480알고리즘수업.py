import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b =map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1,len(graph)):
    graph[j].sort(reverse=True)
    
    
cnt = 0

visited = [0] * (n+1)

def dfs(x,visited):
    global cnt
    cnt += 1
    visited[x] = cnt
    for k in graph[x]:
        if visited[k] == 0:
            dfs(k,visited)
            
dfs(start,visited)
            
for k in range(1,len(visited)):
    print(visited[k])