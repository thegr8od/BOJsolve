n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int,input().split())))
print(data)
k = int(input())
for i in range(k):
    a,b,c,d = map(int, input().split())
    sum = 0
    for j in range(a-1,c):
        for k in range(b-1,d):
            sum += data[j][k]
    print(sum)
