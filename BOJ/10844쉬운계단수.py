n = int(input())

d = [[0] *10 for _ in range(101)]
d[0][0] = 0

for i in range(1,10):
    d[0][i] = 1

for j in range(1,n):
    d[j][0] = d[j-1][1]
    for k in range(1,9):
        d[j][k] = d[j-1][k-1] + d[j-1][k+1]
    d[j][9] = d[j-1][8]

print(sum(d[n-1]) %  1000000000)
