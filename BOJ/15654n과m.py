n,m = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

s = []
 
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in data:
        if i in s:
            continue
        s.append(i)
        dfs(i)
        s.pop()
    
dfs(data[0])