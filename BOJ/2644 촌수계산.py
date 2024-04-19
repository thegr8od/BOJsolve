n = int(input())
start, target = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

result = []

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v,cnt):
    visited[v] = True
    cnt += 1
    if v == target:
        result.append(cnt)
    for i in graph[v]:
        if visited[i] == False:
            dfs(i,cnt)
            
dfs(start,0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)
    
        
        


    
    
    