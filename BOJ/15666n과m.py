n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
s = []

def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    prev = 0
    for i in range(start, n):
        if prev != data[i]:
            s.append(data[i])
            prev = data[i]
            dfs(i)
            s.pop()

dfs(0)