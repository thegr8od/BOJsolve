n = int(input())

d = [1] * 1001


data= list(map(int, input().split()))


for i in range(1,n):
    for j in range(i):
        if data[i] > data[j]:
            d[i] = max(d[i],d[j]+1)


print(max(d))           