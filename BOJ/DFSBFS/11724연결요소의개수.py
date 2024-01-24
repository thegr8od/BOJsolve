import sys

sys.setrecursionlimit(5000)
#sys.setrecursionlimit 함수는 파이썬 인터프리터에서 
#허용하는 최대 재귀 깊이를 설정하는 데 사용
input = sys.stdin.readline

# dfs
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int,input().split())
graph = [ [] for _  in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)