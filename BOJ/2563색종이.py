n = int(input())
cnt= 0

lst = [[0 for i in range(100)] for j in range(100)]

for i in range(n):
    x,y = list(map(int,input().split()))

    for i in range(x, x+10):
        for j in range(y, y+10):
            lst[i][j] = 1

for i in lst:
    cnt += i.count(1)

print(cnt)

