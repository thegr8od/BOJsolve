import sys
input = sys.stdin.readline

N,M = map(int, input().split())

lst = []
for i in range(N):
    lst.append(list(input().split()))

print(lst)
print(lst[0][1])
cnt = 0

for i in range(N):
    for j in range(M):
        if j < M -1:
            if lst[i][j] == lst[i][j+1]:
                lst[i][j+1] = lst[i][j]
                cnt +=1

print(lst)