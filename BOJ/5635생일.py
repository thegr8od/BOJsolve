n = int(input())

data = []
for i in range(n):
    data.append(list(input().split()))

data.sort(key = lambda x: (int(x[-1]),int(x[-2]),int(x[-3])))

print(data[-1][0])
print(data[0][0])