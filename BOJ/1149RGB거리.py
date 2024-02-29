n = int(input())

d = [[0] * 3 for i in range(n)]

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


d[0][0], d[0][1], d[0][2] = data[0][0],data[0][1],data[0][2]

for i in range(1,n):
    d[i][0] = min(d[i-1][1] + data[i][0], d[i-1][2] + data[i][0])
    d[i][1] = min(d[i-1][0] + data[i][1], d[i-1][2] + data[i][1])
    d[i][2] = min(d[i-1][0] + data[i][2], d[i-1][1] + data[i][2])


print(min(d[n-1][0],d[n-1][1],d[n-1][2]))