from collections import deque

n,m = map(int, input().split())


data = list(map(int, input().split()))
data.sort()


s = []
 
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n):
        s.append(data[i])
        dfs(i)
        s.pop()
    



dfs(0)