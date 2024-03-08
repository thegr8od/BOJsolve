n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
visited = [False] * n

s = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, s)))
        return
    prev = 0
    for i in range(N):
        if not visited[i] and prev != data[i]:
            visited[i] = True
            s.append(data[i])
            prev = data[i]
            solve(depth+1, N, M)
            visited[i] = False
            s.pop()

solve(0, n, m)