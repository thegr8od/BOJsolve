import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int, input().split())
visited = [0] * (n+1)
graph= [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



for i in range(1,len(graph)):
    graph[i].sort()
    
cnt = 1
def dfs(v,visited):
    global cnt
    visited[v] = cnt
    cnt += 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i,visited)
            
dfs(r,visited)

for j in range(1,n+1):
    print(visited[j])