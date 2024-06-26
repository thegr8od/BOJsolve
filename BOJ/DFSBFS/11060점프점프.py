n = int(input())
graph = list(map(int, input().split()))
dp = [n+1] * n
dp[0] = 0

for i in range(n):
    for j in range(1, graph[i]+1):
        if i + j < n:
            dp[i+j] = min(dp[i+j], dp[i]+1) 

if dp[-1] == (n+1):
    print(-1)
else:
    print(dp[-1])