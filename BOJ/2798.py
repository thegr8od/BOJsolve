N, M = map(int,input().split())
list = list(map(int, input().split()))
nlist = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            three = list[i]+list[j]+list[k]
            if three <= M:
                nlist.append(three)
            else:
                continue

print(max(nlist))
