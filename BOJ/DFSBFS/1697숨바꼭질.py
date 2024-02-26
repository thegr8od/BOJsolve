from collections import deque
n, k = map(int, input().split())

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x+1,x-1,x*2):
            if nx <= INF and not dist[nx]:
                dist[nx] = dist[x] +1
                queue.append(nx)



INF = 100000
dist = [0] * 100001 
bfs()